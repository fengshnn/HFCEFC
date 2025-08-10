
import numpy as np
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import prepareData1
import tensorflow as tf
from tensorflow.keras.layers import Input, Reshape, Dense, GlobalAveragePooling2D, Concatenate
from tensorflow.keras.applications import ResNet50
# 使用预定义的ResNet18模型
from keras.applications import ResNet50V2 as ResNet18
from tensorflow.keras.models import Model
from tensorflow.keras import regularizers
import os
# 检查并使用第一个可用的GPU
os.environ["CUDA_VISIBLE_DEVICES"] = "0"

# 打印可用的GPU数量
print("Num GPUs Available: ", len(tf.config.experimental.list_physical_devices('GPU')))

# 假设 input1 和 input2 的 shape 都是 (None, 4000)
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
reshaped_input1 = Reshape((2000, 1, 1))(input1)
resized_input1 = tf.image.resize(reshaped_input1, [224, 224])
resized_input1 = Concatenate(axis=-1)([resized_input1, resized_input1, resized_input1])

# 第二个输入通道
input2 = Input(shape=(input_number2,), dtype='float32', name='input2')
reshaped_input2 = Reshape((2000, 1, 1))(input2)
resized_input2 = tf.image.resize(reshaped_input2, [224, 224])
resized_input2 = Concatenate(axis=-1)([resized_input2, resized_input2, resized_input2])

# ResNet50 for first channel with a unique name scope
base_model1 = ResNet18(include_top=False, weights='imagenet', input_tensor=resized_input1)
x1 = base_model1.output
x1 = GlobalAveragePooling2D()(x1)

# ResNet50 for second channel with a unique name scope
base_model2 = ResNet18(include_top=False, weights='imagenet', input_tensor=resized_input2)
x2 = base_model2.output
x2 = GlobalAveragePooling2D()(x2)

# Set unique names for layers in each ResNet50 model to avoid conflicts
for layer in base_model1.layers:
    layer._name = layer.name + '_1'
for layer in base_model2.layers:
    layer._name = layer.name + '_2'

# Concatenate features from both channels
combined_features = Concatenate()([x1, x2])

# Add custom dense layers
x = Dense(64, activation='selu', kernel_regularizer=regularizers.l2(0.0001))(combined_features)
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
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])#  3分类
# model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])#  2分类


# Model summary
model.summary()

# Train the model
model.fit([train_x1, train_x2], train_y, epochs=50, batch_size=200, validation_data=([test_x1, test_x2], test_y))

# Evaluate the model
loss, accuracy = model.evaluate([test_x1, test_x2], test_y)
print(f'Test Loss: {loss}, Test Accuracy: {accuracy}')


# Predictions and evaluation
y_predict1 = model.predict([test_x1, test_x2], batch_size=100, verbose=2)
y_test_pred1 = np.argmax(y_predict1, axis=1)
test_y_true = np.argmax(test_y, axis=1)

print("BCGRES-Resnet18 model classification report:")
print(f"Accuracy: {accuracy_score(test_y_true, y_test_pred1)}")
print(confusion_matrix(test_y_true, y_test_pred1))
print(classification_report(test_y_true, y_test_pred1))

