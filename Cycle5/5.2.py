#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sklearn.cluster import KMeans

from sklearn.datasets import make_blobs

import numpy as np

import matplotlib.pyplot as plt

import seaborn as sns

sns.set()

get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


points, cluster_indexes = make_blobs(n_samples=300, centers=4, cluster_std=0.8, random_state=0)
2
x = points[:, 0]
3
y = points[:, 1]
4
plt.scatter(x, y, s=50, alpha=0.7)


# In[3]:



kmeans = KMeans(n_clusters=4, random_state=0)

kmeans.fit(points)

predicted_cluster_indexes = kmeans.predict(points)

plt.scatter(x, y, c=predicted_cluster_indexes, s=50, alpha=0.7, cmap='viridis')

centers = kmeans.cluster_centers_

plt.scatter(centers[:, 0], centers[:, 1], c='red', s=100)


# In[7]:


inertias = []

for i in range(1, 10):
    kmeans = KMeans(n_clusters=i, random_state=0)
    kmeans.fit(points)

    inertias.append(kmeans.inertia_)

plt.plot(range(1, 10), inertias)

plt.xlabel('Number of clusters')

plt.ylabel('Inertia')


# In[11]:


import pandas as pd

customers = pd.read_csv('customer_data.csv')

customers.head()


# In[12]:


points = customers.iloc[:, 3:5].values

x = points[:, 0]

y = points[:, 1]

plt.scatter(x, y, s=50, alpha=0.7)

plt.xlabel('Annual Income (k$)')

plt.ylabel('Spending Score')


# In[13]:



kmeans = KMeans(n_clusters=5, random_state=0)

kmeans.fit(points)

predicted_cluster_indexes = kmeans.predict(points)

plt.scatter(x, y, c=predicted_cluster_indexes, s=50, alpha=0.7, cmap='viridis')

plt.xlabel('Annual Income (k$)')

plt.ylabel('Spending Score')

centers = kmeans.cluster_centers_

plt.scatter(centers[:, 0], centers[:, 1], c='red', s=100)


# In[18]:



from sklearn.preprocessing import LabelEncoder

df = customers.copy()

encoder = LabelEncoder()

df['Gender'] = encoder.fit_transform(df['Gender'])

df.head()






# In[20]:


points = df.iloc[:, 1:5].values

inertias = []

for i in range(1, 10):

 kmeans = KMeans(n_clusters=i, random_state=0)

 kmeans.fit(points)

 inertias.append(kmeans.inertia_)

plt.plot(range(1, 10), inertias)

plt.xlabel('Number of Clusters')

plt.ylabel('Inertia')


# In[29]:


kmeans = KMeans(n_clusters=5, random_state=0)

kmeans.fit(points)

df['Cluster'] = kmeans.predict(points)

df.head()


# In[32]:


results = pd.DataFrame(columns = ['Cluster', 'Average Age', 'Average Income', 'Average Spending Index', 'Number of Females', 'Number of Males'])

for i in range(len(kmeans.cluster_centers_)):

    age = df[df['Cluster'] == i]['Age'].mean()

    income = df[df['Cluster'] == i]['Annual Income (k$)'].mean()

    spend = df[df['Cluster'] == i]['Spending Score (1-100)'].mean()

    gdf = df[df['Cluster'] == i]

    females = gdf[gdf['Gender'] == 0].shape[0]

    males = gdf[gdf['Gender'] == 1].shape[0]

    results.loc[i] = ([i, age, income, spend, females, males])

results.head()


# In[ ]:




