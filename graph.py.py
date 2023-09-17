#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

df1=pd.read_csv("Fish.csv")
df1

x=list(df1.iloc[:,0])
y=list(df1.iloc[:,1])
plt.bar(x,y)
plt.xlabel('Species')
plt.ylabel('Weight')
plt.title('Weight of each Species')
st.set_option('deprecation.showPyplotGlobalUse', False)
    
BarPlot=plt.show()
st.pyplot(BarPlot)

    


# In[ ]:




