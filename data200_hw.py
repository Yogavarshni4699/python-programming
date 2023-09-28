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
fig, ax = plt.subplots()
sns.heatmap(Churn_df.isnull(), ax=ax)
st.write(fig)

st.write("to know about the dataset")
#Churn_df.columns
Churn_df1=Churn_df.describe()
st.dataframe(Churn_df1)

#checking on the unique value
for i in Churn_df:
  print("No of unique value in",i,"is",Churn_df[i].nunique())
  
st.write("Few findings from the data:")

Churned=Churn_df[Churn_df['Churn']== True].Churn.count()
st.write("No of customers churning:", Churned)

CustChurn_df= Churn_df[Churn_df['Churn']== True]

#unique areacode
areacode=Churn_df['Area code'].nunique()
st.write("No of unique area code",areacode)

#International Plan
International=Churn_df[Churn_df['International plan']=="Yes"]['International plan'].count()
st.write("No of customers having International plan", International)

#Voice mail plan
Voice_mail=Churn_df[Churn_df['Voice mail plan']=="Yes"]['Voice mail plan'].count()
st.write("No of customers having Voice mail plan", Voice_mail)

