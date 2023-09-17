#!/usr/bin/env python
# coding: utf-8

# In[ ]:


drop=st.selectbox("What type of plot to choose?",options=("ScatterPlot","BarPlot","BoxPlot","LinePlot","HistPlot"),index=0,help="Choose a plot option in dropdown",disabled=False)
st.write("You chose", drop,"Chart")

df1=pd.read_csv("fish.csv")
df1
if drop=="ScatterPlot":
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
    
else drop=="BarPlot":

    x=list(df1.iloc[:,0])
    y=list(df1.iloc[:,1])
    plt.bar(x,y)
    plt.xlabel('Species')
    plt.ylabel('Weight')
    plt.title('Weight of each Species')
    
    BarPlot=plt.show()

