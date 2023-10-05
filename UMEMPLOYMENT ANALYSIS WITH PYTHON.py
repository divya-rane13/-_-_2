#!/usr/bin/env python
# coding: utf-8

# # Importing neccessary python libraries 

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


# # Importing data

# In[3]:


data=pd.read_csv("Unemployment_Rate_upto_11_2020.csv")
data.head()


# In[4]:


print(data.isnull().sum())


# In[5]:


data.columns= ["States","Date","Frequency",
               "Estimated Unemployment Rate",
               "Estimated Employed",
               "Estimated Labour Participation Rate",
               "Region","longitude","latitude"]


# # Unemployment  Rate AnalAnalysis : Data Visualization

# In[6]:


data1=data.drop("States",axis=1)
data2=data1.drop("Region",axis=1)
data3=data2.drop("Date",axis=1)
data4=data3.drop("Frequency",axis=1)


# In[7]:


sns.heatmap(data4.corr())


# # Unemployment Rate Analysis: Data Visualization

# In[8]:


plt.title("Indian Unemployment")
sns.histplot(x="Estimated Employed", hue="Region", data=data)
plt.show()


# # Unemployment according to states

# In[10]:


unemploment = data[["States", "Region", "Estimated Unemployment Rate"]]
figure = px.sunburst(unemploment, path=["Region", "States"], 
                     values="Estimated Unemployment Rate", 
                     width=700, height=700, color_continuous_scale="RdY1Gn", 
                     title="Unemployment Rate in India")
figure.show()


# In[ ]:




