from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn import datasets
# from keras.layers import *
# import keras.layers as KL
# import keras.backend as K
# from keras import Model
# from keras.utils import  to_categorical
# from keras.utils.vis_utils import plot_model
import pandas as pd
import numpy as np
# import tensorflow as tf
# from keras import regularizers

from sklearn.utils import shuffle
# import matplotlib.pyplot as plt
# import keras
import prepareData1

z = np.concatenate([np.array(prepareData1.train_XGBT),np.array(prepareData1.train_y_1.reshape((-1, 1)))],axis=1)
z = pd.DataFrame(z)
z.to_csv('OnlyXGBT_data/train_features.csv',index=False)

z = np.concatenate([np.array(prepareData1.test_XGBT),np.array(prepareData1.test_y_1.reshape((-1, 1)))],axis=1)
z = pd.DataFrame(z)
z.to_csv('OnlyXGBT_data/test_features.csv',index=False)

# XGBT
import xgboost

# 导入训练集和标签
train = pd.read_csv('OnlyXGBT_data/train_features.csv')
train_labels_xg = train['33'].astype('int')  # lable
train_feats_xg = train.drop(['33'],axis=1) # features,33,57

dataset = xgboost.DMatrix(train_feats_xg, label=train_labels_xg)
watchlist = [(dataset, 'train')]
# params = {'max_depth':10, 'eta':0.1, 'silent':1, 'num_class':2,'objective':'multi:softmax' }
params = {'max_depth':10, 'eta':0.1, 'silent':1, 'num_class':3,'objective':'multi:softmax' }
model_xg = xgboost.train(params, dataset, num_boost_round=120, evals=watchlist)

test = pd.read_csv('OnlyXGBT_data/test_features.csv')
test_labels_xg = test['33'].astype('int')
test_feats_xg = test.drop(['33'],axis=1)

test_x = xgboost.DMatrix(test_feats_xg)
xgbt_result = model_xg.predict(test_x)
z = pd.DataFrame(xgbt_result)

z.to_csv('OnlyXGBT_data/result_test.csv',index=False)
print(classification_report(test_labels_xg, xgbt_result))
print(confusion_matrix(test_labels_xg, xgbt_result))
XGBT_accuracy = accuracy_score(test_labels_xg, xgbt_result)
print("test_labels_xg:",test_labels_xg)
print("真实：",prepareData1.test_y_1)
print("xgbt_result:",xgbt_result)

print("XGBT_accuracy:",XGBT_accuracy)


# #画出混淆矩阵
# from sklearn import metrics as met
# import Plot1
# labels_dict_inv = ['0', '1']
# cm = met.confusion_matrix(test_labels_xg, xgbt_result)
# Plot1.plot_confusion_matrix(cm,
#                       normalize    = False,
#                       target_names = labels_dict_inv,
#                       title        = "Confusion Matrix")
# Plot1.plot_confusion_matrix(cm,
#                       normalize    = True,
#                       target_names = labels_dict_inv,
#                       title        = "Confusion Matrix")


