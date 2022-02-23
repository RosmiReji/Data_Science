#!/usr/bin/env python
# coding: utf-8

# In[7]:



from nltk.corpus import stopwords
import nltk
from nltk.tokenize import sent_tokenize,word_tokenize
text1 = "The data set given satisfies the requirement for model generation. This is used in Data Science Lab"
print(sent_tokenize(text1))
print(word_tokenize(text1))
print(stopwords.words('english'))
text = word_tokenize(text1)
text= [word for word in text if word not in stopwords.words('english')]
print(text)
print(nltk.pos_tag(text))
temp=zip(*[text[i:] for i in range(0,2)])
ans=[' '.join(ngram) for ngram in temp]
print(ans)
temp=zip(*[text[i:] for i in range(0,4)])
ans=[' '.join(ngram) for ngram in temp]
print(ans)


# In[ ]:





# In[2]:


nltk.download('punkt')


# In[4]:


nltk.download('stopwords')


# In[6]:


nltk.download('averaged_perceptron_tagger')


# In[ ]:




