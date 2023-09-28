import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#read the data
Churn_df = pd.read_csv('/content/Telecom Churn.csv')
st.write("Data:")
st.write(Churn_df.head())


#check duplicate
Churn_df.duplicated().sum()

#Missing Values/ Null Values
Churn_df.isnull().sum()

#Visualizing null value
# Display the heatmap
st.write("Heatmap of Missing Data (NaN values):")
plot = sns.heatmap(Churn_df.isnull(), annot=True) 
# Display the plot in Streamlit
st.pyplot(plot.get_figure())

#to know about the dataset
Churn_df.columns
Churn_df.describe()

#checking on the unique value
for i in Churn_df:
  print("No of unique value in",i,"is",Churn_df[i].nunique())

st.write("Few findings from the data:")

st.write("No of customers churning:", Churn_df[Churn_df['Churn']== True].Churn.count())
CustChurn_df= Churn_df[Churn_df['Churn']== True]

#unique areacode
st.write("No of unique area code",Churn_df['Area code'].nunique())

#International Plan
st.write("No of customers having International plan", Churn_df[Churn_df['International plan']=="Yes"]['International plan'].count())

#Voice mail plan
st.write("No of customers having Voice mail plan", Churn_df[Churn_df['Voice mail plan']=="Yes"]['Voice mail plan'].count())

CustChurn_df

# % of total custom churning
st.write("Total customers", Churn_df.Churn.count())
# % of churn
Perc_churn= (CustChurn_df.Churn.count()/Churn_df.Churn.count()*100)
st.write(f"Percentage of Customer Churn: {round(Perc_churn,2)} %")

st.write("State Wise Customer Churning")
State_cus_churn = CustChurn_df.groupby(['States'])['Churn'].value_counts().reset_index(name='Churn_Customers')
st.write(State_cus_churn.sum())
State_cus_churn

#Area Code wise Churn Counts
Area_code_churn_count= CustChurn_df.groupby(['Area code'])['Churn'].value_counts().reset_index(name="Count")
Area_code_churn_count

#Chart-1
print(Churn_df.Churn.value_counts())
print("")
Churn_df['Churn'].value_counts().plot(kind='pie',figsize=(10,6),autopct="%1.1f%%", startangle=50,shadow=True,labels=['Not Churn %','Churn %'],
                             colors=['green','red'],explode=[0.12,0])
st.write(plt.title("Total Percentage of Churn"))
#Display Chart
st.plt.show()

st.write("From the above chart we got to know that , there are 2850 customers not churned which is 85.5% of the whole customer data given in the dataset. 
In othger words,  483 customers are churned which is 14.5%. It is not very high
but still churn is bad for business. So churn rate insights are very helpful for furthur decisions.")
