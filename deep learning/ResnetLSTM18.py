from keras.utils import plot_model
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import prepareData1

import tensorflow as tf
from tensorflow.keras.layers import Input, Reshape, Add,Subtract,Multiply,Dense, GlobalAveragePooling2D, Concatenate, Bidirectional, LSTM, BatchNormalization, Dropout, Flatten
from tensorflow.keras.applications import ResNet50
# 使用预定义的ResNet18模型
from keras.applications import ResNet50V2 as ResNet18
from tensorflow.keras.models import Model
from tensorflow.keras import regularizers
import numpy as np
import pandas as pd
import os
from keras.layers import Lambda
# 检查并使用第一个可用的GPU
os.environ["CUDA_VISIBLE_DEVICES"] = "0"

# 打印可用的GPU数量
print("Num GPUs Available: ", len(tf.config.experimental.list_physical_devices('GPU')))



# 假设 input1 和 input2 的 shape 都是 (None, 4000),20s:4000;10s :2000
input_number1 = 2000
input_number2 = 2000
train_x1 = prepareData1.train_x_1
train_y = prepareData1.train_y_ohe
test_x1 = prepareData1.test_x_1
test_y = prepareData1.test_y_ohe

train_x2 = prepareData1.train_x_2
test_x2 = prepareData1.test_x_2

# 第一个输入通道
input1 = Input(shape=(input_number1,), dtype='float32', name='input1')
reshaped_input1 = Reshape((2000, 1, 1))(input1)  #20s:800, 5, 1;10s:1000,2,1
resized_input1 = tf.image.resize(reshaped_input1, [224, 224])
resized_input1 = Concatenate(axis=-1)([resized_input1, resized_input1, resized_input1])

# 第二个输入通道
input2 = Input(shape=(input_number2,), dtype='float32', name='input2')
reshaped_input2 = Reshape((2000, 1, 1))(input2)#20s:2000, 2, 1
resized_input2 = tf.image.resize(reshaped_input2, [224, 224])
resized_input2 = Concatenate(axis=-1)([resized_input2, resized_input2, resized_input2])


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

# ResNet50 for first channel with a unique name scope
with tf.keras.utils.custom_object_scope({'tf': tf}):
    base_model1 = ResNet18(include_top=False, weights='imagenet', input_tensor=resized_input1)
    for layer in base_model1.layers:
        layer._name = layer.name + '_1'

x1 = base_model1.output
x1 = GlobalAveragePooling2D()(x1)

# LSTM for first channel (after ResNet)
lstm_input1 = Reshape((1, -1))(x1)
lstm1 = Bidirectional(LSTM(50, return_sequences=True))(lstm_input1)
lstm1 = BatchNormalization()(lstm1)
lstm1 = Dropout(0.5)(lstm1)
lstm1 = Flatten()(lstm1)

# ResNet50 for second channel with a unique name scope
with tf.keras.utils.custom_object_scope({'tf': tf}):
    base_model2 = ResNet18(include_top=False, weights='imagenet', input_tensor=resized_input2)
    for layer in base_model2.layers:
        layer._name = layer.name + '_2'

x2 = base_model2.output
x2 = GlobalAveragePooling2D()(x2)

# LSTM for second channel (after ResNet)
lstm_input2 = Reshape((1, -1))(x2)
lstm2 = Bidirectional(LSTM(25, return_sequences=True))(lstm_input2)
lstm2 = BatchNormalization()(lstm2)
lstm2 = Dropout(0.5)(lstm2)
lstm2 = Flatten()(lstm2)

# Concatenate features from ResNet50 and BiLSTM for both channels
# combined_features = Concatenate()([lstm1, lstm2])
combined_features = Add()([lstm1, lstm2])
# combined_features = Subtract()([lstm1, lstm2])
# combined_features = Multiply()([lstm1, lstm2])
# epsilon = 1e-7  # 一个非常小的数，避免除零
# combined_features = Lambda(lambda x: x[0] / (x[1] + epsilon))([lstm1, lstm2])

# Add custom dense layers
x = Dense(64, activation='selu', kernel_regularizer=regularizers.l2(0.0005))(combined_features)
# x = Dense(64, activation='selu', kernel_regularizer=regularizers.l2(0.0001))(combined_features)
output = Dense(3, activation='softmax')(x)# 3 分类
# output = Dense(2, activation='sigmoid')(x)  # 2 分类

# Create the model
model = Model(inputs=[input1, input2], outputs=output)

# Freeze ResNet50 layers
for layer in base_model1.layers:
    layer.trainable = False

for layer in base_model2.layers:
    layer.trainable = False

# Compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
# model.compile(optimizer='adam', loss=weighted_categorical_crossentropy(class_weights), metrics=['accuracy'])
# model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])#  2分类

# Model summary
model.summary()
plot_model(model, to_file='model-ResNet.png', show_shapes=True)  # 查看model 网络结构
# Train the model
model.fit([train_x1, train_x2], train_y, epochs=50, batch_size=200, validation_data=([test_x1, test_x2], test_y))

# Evaluate the model
loss, accuracy = model.evaluate([test_x1, test_x2], test_y)
print(f'Test Loss: {loss}, Test Accuracy: {accuracy}')

# Predictions and evaluation
y_predict1 = model.predict([test_x1, test_x2], batch_size=100, verbose=2)
y_test_pred1 = np.argmax(y_predict1, axis=1)
test_y_true = np.argmax(test_y, axis=1)

print("BCGRES-Resnet18BILSTM model classification report:")
print(f"Accuracy: {accuracy_score(test_y_true, y_test_pred1)}")
print(confusion_matrix(test_y_true, y_test_pred1))
print(classification_report(test_y_true, y_test_pred1))


# # Create a model to output the features from the dense layer
# feature_model = Model(inputs=[input1, input2], outputs=x)
#
# # Get features for the training set
# train_feat_map_np = feature_model.predict([train_x1, train_x2], batch_size=100, verbose=2)
#
# # Combine with hand-crafted features and labels
# z = np.concatenate([np.array(prepareData1.train_XGBT), np.array(prepareData1.train_y_1.reshape((-1, 1))), np.array(train_feat_map_np)], axis=1)
# z = pd.DataFrame(z)
# z.to_csv('merged_data/train_features.csv', index=False)
#
# # Get features for the test set
# test_feat_map_np = feature_model.predict([test_x1, test_x2], batch_size=30, verbose=2)
#
# # Combine with hand-crafted features and labels
# z = np.concatenate([np.array(prepareData1.test_XGBT), np.array(prepareData1.test_y_1.reshape((-1, 1))), np.array(test_feat_map_np)], axis=1)
# z = pd.DataFrame(z)
# z.to_csv('merged_data/test_features.csv', index=False)
