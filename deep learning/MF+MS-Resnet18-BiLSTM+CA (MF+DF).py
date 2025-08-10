import tensorflow as tf
from tensorflow.keras.layers import Input, Dense, Dropout, Concatenate, MultiHeadAttention, Flatten, Lambda
from tensorflow.keras.models import Model
from tensorflow.keras import regularizers
import numpy as np
import pandas as pd
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from keras.utils import plot_model

# 加载数据
train = pd.read_csv('merged_data/train_features.csv')
train_labels = train['33'].astype('int')
train_feats = train.drop(['33'], axis=1).values

test = pd.read_csv('merged_data/test_features.csv')
test_labels = test['33'].astype('int')
test_feats = test.drop(['33'], axis=1).values

# Convert labels to one-hot encoding
train_labels_ohe = tf.keras.utils.to_categorical(train_labels, num_classes=3) # 3分类
test_labels_ohe = tf.keras.utils.to_categorical(test_labels, num_classes=3)

# Define input shapes
input_shape = train_feats.shape[1]
handcrafted_features_dim = 33  # 手工特征的维度
deep_features_dim = input_shape - handcrafted_features_dim

# Define the model
input_layer = Input(shape=(input_shape,), name='input_layer')

# Split input into handcrafted features and deep features using Lambda layers
handcrafted_feat_input = Lambda(lambda x: x[:, :handcrafted_features_dim])(input_layer)  # 前33列是手工特征
deep_feat_input = Lambda(lambda x: x[:, handcrafted_features_dim:])(input_layer)  # 其余是深度特征

# Project features to the same dimensionality
projected_handcrafted_feat = Dense(20, activation='relu')(handcrafted_feat_input)
projected_deep_feat = Dense(20, activation='relu')(deep_feat_input)

# Reshape inputs for attention mechanism
projected_handcrafted_feat_reshaped = tf.expand_dims(projected_handcrafted_feat, axis=1)
projected_deep_feat_reshaped = tf.expand_dims(projected_deep_feat, axis=1)

# Cross-Attention mechanism
attention_output = MultiHeadAttention(num_heads=1, key_dim=20)(query=projected_handcrafted_feat_reshaped,
                                                               value=projected_deep_feat_reshaped,
                                                               key=projected_deep_feat_reshaped)
attention_output = Flatten()(attention_output)

# Combine features
combined_features = Concatenate()([projected_handcrafted_feat, projected_deep_feat, attention_output])

# Add custom dense layers
x = Dense(10, activation='selu', kernel_regularizer=regularizers.l2(0.0001))(combined_features)
x = Dropout(0.5)(x)
output = Dense(3, activation='softmax')(x)
# output = Dense(2, activation='sigmoid')(x)  # 2 分类

# Create the model
attention_model = Model(inputs=input_layer, outputs=output)

# Compile the model
attention_model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])#  3分类
# attention_model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])#  2分类

# Model summary
# attention_model.summary()
# plot_model(attention_model, to_file='attention_model.png', show_shapes=True)  # 查看model 网络结构

# Train the model
attention_model.fit(train_feats, train_labels_ohe, epochs=50, batch_size=32, validation_data=(test_feats, test_labels_ohe))

# Evaluate the model
loss, accuracy = attention_model.evaluate(test_feats, test_labels_ohe)
print(f'Test Loss: {loss}, Test Accuracy: {accuracy}')

# Predict and evaluate
y_pred = attention_model.predict(test_feats)
y_pred_classes = np.argmax(y_pred, axis=1)

print("CrossAttention-based model classification report:")
print(classification_report(test_labels, y_pred_classes))
print("Confusion matrix:")
print(confusion_matrix(test_labels, y_pred_classes))

# 计算分类准确率
accuracy = accuracy_score(test_labels, y_pred_classes)
print(f'Classification Accuracy: {accuracy}')
