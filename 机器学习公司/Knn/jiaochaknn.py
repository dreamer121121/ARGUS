# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#交叉验证法寻找最优KNN的K值
import os
import numpy as np
import pandas as pd
from sklearn import neighbors
from sklearn.model_selection import cross_val_score
#处理数据
os.chdir(r'C:\Users\outao\Desktop\机器学习\机器学习数据集\Datasets\Breast-Cancer')
train_data=pd.read_csv('breast-cancer-train.csv')
test_data=pd.read_csv('breast-cancer-test.csv')
train_x=train_data.iloc[:,1:30]
train_y=train_data.iloc[:,31]
test_x=test_data.iloc[:,1:31]
test_y=test_data.iloc[:,31]
k_scores={}
for k in range(1,300):
    #构建分类器
    knn=neighbors.KNeighborsClassifier(n_neighbors=k)
    scores=cross_val_score(knn,train_x,train_y,cv=10,n_jobs=1)
    k_scores[k]=scores.mean()
best_k=1
for key in k_scores:
    if k_scores[best_k]<k_scores[key]:
        besk_k=key
    else:
        continue
print (str(best_k)+':'+str(k_scores[best_k]))
        

    
    
    










        









