import pandas as pd
import csv
import matplotlib.pyplot as plt
import streamlit as st


df1=pd.read_csv("fish.csv")
df1
st.write("Here is my first attempt to use streamlit")
    
x=list(df1.iloc[:,1])
y=list(df1.iloc[:,6])
plt.scatter(x,y)
plt.xlabel('Weight')
plt.ylabel('Width')
plt.title('Weight to Width of species')
ScatterPlot=plt.show()
st.title("Plots Example")
st.set_option('deprecation.showPyplotGlobalUse', False)
st.pyplot(ScatterPlot)
    
