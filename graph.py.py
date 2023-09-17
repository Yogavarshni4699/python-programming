#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

drop=st.selectbox("What type of plot to choose?",options=("BarPlot","No Plot"),index=0,help="Choose a plot option in dropdown")
st.write("You chose", drop,"Chart")

df1=pd.read_csv("fish.csv")
df1
if drop=="BarPlot":

    x=list(df1.iloc[:,0])
    y=list(df1.iloc[:,1])
    plt.bar(x,y)
    plt.xlabel('Species')
    plt.ylabel('Weight')
    plt.title('Weight of each Species')
    
    BarPlot=plt.show()
    st.pyplot(BarPlot)

    


# In[ ]:




