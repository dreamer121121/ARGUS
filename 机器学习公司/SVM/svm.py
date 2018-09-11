from sklearn import svm,datasets
import numpy as np
import pandas as pd
from sklearn import neighbors
data=datasets.load_breast_cancer()
train_X=data['data'][0:299,:]
test_X=data['data'][300:,:]
train_y=data['target'].tolist()[0:299]
test_y=data['target'].tolist()[300:]
clf=svm.SVC(kernel='linear')
clf.fit(train_X,train_y)
result=clf.predict(test_X)
#score=clf.score(test_X,test_y)
#print (score)
error=[]
for i in range(269):
    if result[i]!=test_y[i]:
        error.append(i)
    else:
        continue   
error_sample=[]
for j in error:
    error_sample.append(train_X[j,:])
print (error_sample)



