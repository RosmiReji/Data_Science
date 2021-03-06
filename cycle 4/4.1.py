#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
dataset = pd.read_csv("iris.csv")
dataset.head()
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 4].values
print("X values :\n",X)
print("--------------------")
print("Y values:\n",y)


# In[22]:


from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.30)
from sklearn.neighbors import KNeighborsClassifier
Classifier=KNeighborsClassifier(n_neighbors=15)
classifier.fit(X_train,y_train)
y_pred=classifier.predict(X_test)
from sklearn.metrics import accuracy_score
accuracy=accuracy_score(y_test,y_pred)
print("Accuracy",accuracy)


# In[ ]:


for(i,j) in zip(y_pred,y_test):
    if(i!=j):
        print("actual:",i,"predicted value",j)
        print("")
        print("Number of mislabeled points from test data set")


# In[26]:


from sklearn.metrics import classification_report,confusion_matrix
print(".....Confusion matrix........")
print("")
print(confusion_matrix(y_test,y_pred))
print("....Classification Report.....")
print(classification_report(y_test,y_pred))
 
      


# In[ ]:





# In[ ]:




