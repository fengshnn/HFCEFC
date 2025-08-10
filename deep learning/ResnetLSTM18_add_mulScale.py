from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import prepareData1
from keras.utils import plot_model
import tensorflow as tf
from tensorflow.keras.layers import Input, Reshape, Dense, GlobalAveragePooling1D, Multiply, Bidirectional, LSTM, BatchNormalization, Dropout, Flatten, Conv1D, MaxPooling1D, Add, Activation
from tensorflow.keras.models import Model
from tensorflow.keras import regularizers
import numpy as np
import pandas as pd
import os

# 检查并使用第一个可用的GPU
os.environ["CUDA_VISIBLE_DEVICES"] = "0"

# 打印可用的GPU数量
print("Num GPUs Available: ", len(tf.config.experimental.list_physical_devices('GPU')))

# 假设 input1 和 input2 的 shape 都是 (None, 2000)
input_number1 = 2000
input_number2 = 2000
train_x1 = prepareData1.train_x_1
train_y = prepareData1.train_y_ohe
test_x1 = prepareData1.test_x_1
test_y = prepareData1.test_y_ohe

train_x2 = prepareData1.train_x_2
test_x2 = prepareData1.test_x_2

# 多尺度输入
def create_multiscale_input(input_tensor, scales=[1,2,4]):
    multiscale_outputs = []
    for scale in scales:
        reshaped_input = Reshape((input_tensor.shape[1] // scale, scale))(input_tensor)  # reshape to (batch_size, new_length, scale)
        conv = Conv1D(filters=64, kernel_size=3, activation='relu', padding='same')(reshaped_input)
        pool = MaxPooling1D(pool_size=2)(conv)
        multiscale_outputs.append(pool)
    return multiscale_outputs

# 特征拼接
def concatenate_multiscale_features(multiscale_inputs):
    concatenated_features = tf.keras.layers.Concatenate(axis=1)(multiscale_inputs)  # Concatenate along the time axis
    return concatenated_features

# ResNet18 一维残差块
def resnet_block_1d(input_tensor, filters, strides=1):
    x = Conv1D(filters, 3, strides=strides, padding='same')(input_tensor)
    x = BatchNormalization()(x)
    x = Activation('relu')(x)
    x = Conv1D(filters, 3, strides=1, padding='same')(x)
    x = BatchNormalization()(x)

    if strides != 1 or input_tensor.shape[-1] != filters:
        shortcut = Conv1D(filters, 1, strides=strides, padding='same')(input_tensor)
        shortcut = BatchNormalization()(shortcut)
    else:
        shortcut = input_tensor

    x = Add()([x, shortcut])
    x = Activation('relu')(x)
    return x

# ResNet18 一维模型
def resnet18_1d(input_shape):
    input_tensor = Input(shape=input_shape)
    x = Conv1D(64, 7, strides=2, padding='same')(input_tensor)
    x = BatchNormalization()(x)
    x = Activation('relu')(x)
    x = MaxPooling1D(3, strides=2, padding='same')(x)

    x = resnet_block_1d(x, 64)
    x = resnet_block_1d(x, 64)
    x = resnet_block_1d(x, 128, strides=2)
    x = resnet_block_1d(x, 128)
    x = resnet_block_1d(x, 256, strides=2)
    x = resnet_block_1d(x, 256)
    x = resnet_block_1d(x, 512, strides=2)
    x = resnet_block_1d(x, 512)

    x = GlobalAveragePooling1D()(x)
    model = Model(inputs=input_tensor, outputs=x)
    return model

# 使用ResNet18模型提取特征并使用BiLSTM处理
def resnet_bilstm_model(input_tensor, suffix):
    input_shape = (input_tensor.shape[1], input_tensor.shape[2])
    resnet_model = resnet18_1d(input_shape)
    x = resnet_model(input_tensor)
    lstm_input = Reshape((1, -1))(x)
    lstm = Bidirectional(LSTM(25, return_sequences=True))(lstm_input)
    lstm = BatchNormalization()(lstm)
    lstm = Dropout(0.5)(lstm)
    lstm = Flatten()(lstm)
    return lstm

# 加权交叉熵损失函数
def weighted_categorical_crossentropy(weights):
    weights = tf.constant(weights)
    def loss(y_true, y_pred):
        y_pred = tf.clip_by_value(y_pred, tf.keras.backend.epsilon(), 1 - tf.keras.backend.epsilon())
        y_true = tf.cast(y_true, dtype='float32')
        loss = y_true * tf.math.log(y_pred) * weights
        loss = -tf.reduce_sum(loss, axis=-1)
        return loss
    return loss

# 根据数据分布定义类别权重
class_weights = np.sum(train_y, axis=0)
class_weights = class_weights / np.sum(class_weights)
class_weights = 1.0 / class_weights
class_weights = class_weights / np.sum(class_weights)

# 第一个输入通道（BCG信号）
input1 = Input(shape=(input_number1,), dtype='float32', name='input1')
multiscale_input1 = create_multiscale_input(input1)
concatenated_features1 = concatenate_multiscale_features(multiscale_input1)
resnet_bilstm_features1 = resnet_bilstm_model(concatenated_features1, '1')

# 第二个输入通道（RES信号）
input2 = Input(shape=(input_number2,), dtype='float32', name='input2')
multiscale_input2 = create_multiscale_input(input2)
concatenated_features2 = concatenate_multiscale_features(multiscale_input2)
resnet_bilstm_features2 = resnet_bilstm_model(concatenated_features2, '2')

# Combine features by addition
combined_features = Add()([resnet_bilstm_features1, resnet_bilstm_features2])
# Add custom dense layers
x = Dense(64, activation='selu', kernel_regularizer=regularizers.l2(0.0005))(combined_features)
output = Dense(3, activation='softmax')(x)
# output = Dense(2, activation='sigmoid')(x)  # 2 分类

# Create the model
model = Model(inputs=[input1, input2], outputs=output)

# Compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])#  3分类
# model.compile(optimizer='adam', loss=weighted_categorical_crossentropy(class_weights), metrics=['accuracy'])
# model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])#  2分类

# Model summary
model.summary()
plot_model(model, to_file='model-ResNet.png', show_shapes=True)  # 查看model 网络结构

# Train the model with smaller batch size
model.fit([train_x1, train_x2], train_y, epochs=50, batch_size=200, validation_data=([test_x1, test_x2], test_y))

# Evaluate the model
loss, accuracy = model.evaluate([test_x1, test_x2], test_y)
print(f'Test Loss: {loss}, Test Accuracy: {accuracy}')

# Predictions and evaluation
y_predict1 = model.predict([test_x1, test_x2], batch_size=100, verbose=2)
y_test_pred1 = np.argmax(y_predict1, axis=1)
test_y_true = np.argmax(test_y, axis=1)

print("mulscale-BCGRES-Resnet18BILSTM-4 model classification report:")
print(f"Accuracy: {accuracy_score(test_y_true, y_test_pred1)}")
print(confusion_matrix(test_y_true, y_test_pred1))
print(classification_report(test_y_true, y_test_pred1))

# Create a model to output the features from the dense layer
feature_model = Model(inputs=[input1, input2], outputs=x)

# Get features for the training set
train_feat_map_np = feature_model.predict([train_x1, train_x2], batch_size=100, verbose=2)

# Combine with hand-crafted features and labels
z = np.concatenate([np.array(prepareData1.train_XGBT), np.array(prepareData1.train_y_1.reshape((-1, 1))), np.array(train_feat_map_np)], axis=1)
z = pd.DataFrame(z)
z.to_csv('merged_data/train_features.csv', index=False)

# Get features for the test set
test_feat_map_np = feature_model.predict([test_x1, test_x2], batch_size=50, verbose=2)

# Combine with hand-crafted features and labels
z = np.concatenate([np.array(prepareData1.test_XGBT), np.array(prepareData1.test_y_1.reshape((-1, 1))), np.array(test_feat_map_np)], axis=1)
z = pd.DataFrame(z)
z.to_csv('merged_data/test_features.csv', index=False)
