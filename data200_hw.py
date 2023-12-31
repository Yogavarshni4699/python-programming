import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#read the data
Churn_df = pd.read_csv("Telecom_Churn.csv")
st.write("Data - Telecom Churn:")
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

st.write("To know about the dataset")
Churn_df1=Churn_df.describe()
st.dataframe(Churn_df1)

st.write("Few findings from the data:")

Churned=Churn_df[Churn_df['Churn']== True].Churn.count()
st.write("No of customers churning:", Churned)
CustChurn_df= Churn_df[Churn_df['Churn']== True]

#unique areacode
areacode=Churn_df['Area code'].nunique()
st.write("No of unique area code:",areacode)

#International Plan
International=Churn_df[Churn_df['International plan']=="Yes"]['International plan'].count()
st.write("No of customers having International plan:", International)

#Voice mail plan
Voice_mail=Churn_df[Churn_df['Voice mail plan']=="Yes"]['Voice mail plan'].count()
st.write("No of customers having Voice mail plan:", Voice_mail)

# % of total custom churning
Total_cut_churn=Churn_df.Churn.count()
st.write("Total customers:",Total_cut_churn)
# % of churn
Perc_churn= (CustChurn_df.Churn.count()/Churn_df.Churn.count()*100)
#{round(Perc_churn,2)} %
st.write("Percentage of Customer Churn in %:", Perc_churn)

st.write("State Wise Customer Churning")
State_cus_churn = CustChurn_df.groupby(['States'])['Churn'].value_counts().reset_index(name='Churn_Customers')
#Summed= State_cus_churn.sum()
st.dataframe(State_cus_churn)

st.write("State TX has the highest number of churn")

# Display the chart using Streamlit
fig, ax = plt.subplots()
Churn_df['Churn'].value_counts().plot(kind='pie', figsize=(10, 6), autopct="%1.1f%%", startangle=50, shadow=True,
                  labels=['Not Churn %', 'Churn %'], colors=['green', 'red'], explode=[0.12, 0])
plt.title("Total Percentage of Churn")

# Display the chart using Streamlit
st.pyplot(fig)

st.write("From the chart we got to know that there are 2850 customers not churned which is 85.5% of the whole customer data given in the dataset. In other words, 483 customers are churned which is 14.5%. It is not very high but still, churn is bad for business. So churn rate insights are very helpful for further decisions")
