import streamlit as st 
import pandas as pd 
import numpy as np



### Title of application 
st.title("Hello streamlit")

## Display simple text 
st.write("This is a simple Text")

### Create A simple Data Frame 
df=pd.DataFrame({
    'first_column':[1,2,3,4],
    'second column':[10,20,30,40]
})

## Display the DataFrame
st.write('Here Is the dataframe')
st.write(df)

## create a line chart
chart_data=pd.DataFrame(
    np.random.randn(20,3),columns=['a','b','c']
                        )
st.line_chart(chart_data)



