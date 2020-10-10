#!/usr/bin/env python
# coding: utf-8

# In[1]:


#install and import matplotlib
import matplotlib.pyplot as plt


# In[2]:


#matplotlib to render plots in the notebook
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


x=[-3,5,7]


# In[4]:


x


# In[5]:


y=[10,2,5]


# In[6]:


y


# In[7]:


fig = plt.figure(figsize=(15,3))

plt.plot(x,y)

plt.xlim(0,10)
plot.tlim(-3,8)

plt.xlabel('X Axis')
plt.ylabel('Y Axis')


plt.title('Line Plot')

plt.suptitle("Sales Comparison", size=20,y=1.03)


# In[8]:


#fig.savefig('example.png')


# In[11]:


###How to change the plot size

fig.set_size_inches(14,4)


# In[12]:


fig


# In[13]:


####The subplots functions returns a two-item tuple object containingf the Figure and one or more Axes objects(here it is just one), which is unpacked into variables fig and ax


# In[14]:


fig,ax=plt.subplots(nrows=1,ncols=1)


# In[15]:


#More thaqn one axes with plt.subplots, then the second item in the tupleis a numpy array containing all the axes

fig,axs=plt.subplots(2,4)


# In[3]:


### Matplotlib

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[5]:


mtcars=pd.read_csv("F:\\Python\\mtcars.csv")


# In[6]:


mtcars


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[7]:


mtcars.columns


# In[ ]:





# In[ ]:





# In[8]:


mtcars.shape


# In[ ]:





# In[9]:


mtcars.head()


# In[ ]:





# In[11]:


#table
pd.crosstab(mtcars.gear,mtcars.cyl)


# In[ ]:





# In[ ]:





# In[12]:


#Bar Plot Between 2 different categories
pd.crosstab(mtcars.gear,mtcars.cyl).plot(kind="bar")


# In[ ]:





# In[14]:


mtcars["gear"].value_counts()


# In[ ]:





# In[ ]:





# In[15]:


mtcars.gear.value_counts().plot(kind="pie")


# In[ ]:




