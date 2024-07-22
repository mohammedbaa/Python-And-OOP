import streamlit as st 
import pandas as pd 


st.title('Streamlit Text Input')

name=st.text_input("Enter your name:")

age=st.slider("select your age:",0,100,25)

st.write(f"your age is {age}.")

options=['Python','Java','C++','Java Script']
choise=st.selectbox("choose your Favorite language",options)
st.write(f"you selected {choise}.")

if name :
    st.write(f'Hello,{name}') 


data={
    "Name":["John","Jane","Jake","Jill"],
    "Age":[28,24,35,40],
    "City":['New Yourk',"Los Angeles",'Chicago','Houston']
}

df=pd.DataFrame(data)
df.to_csv('sampledata.csv')
st.write(df)


uploded_files=st.file_uploader("Choose A CSV File",type="csv")

if uploded_files is not None : 
    df=pd.read_csv(uploded_files)
    st.write(df) 
