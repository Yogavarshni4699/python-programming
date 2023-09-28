import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#read the data
Churn_df = pd.read_csv("Telecom_Churn.csv")
st.write("Data:")
Churn_df.head()
st.dataframe(Churn_df)

#check duplicate
Churn_df.duplicated().sum()

#Missing Values/ Null Values
Churn_df.isnull().sum()

#Visualizing null value
# Display the heatmap
st.write("Heatmap to check Missing Data:")
plot = sns.heatmap(Churn_df.isnull(), annot=True) 
# Display the plot in Streamlit
st.pyplot(plot.get_figure())

#to know about the dataset
Churn_df.columns
Churn_df1=Churn_df.describe()
st.dataframe(Churn_df1)


