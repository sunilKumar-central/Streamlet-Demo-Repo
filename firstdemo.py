import streamlit as st
import pandas as pd 
import numpy as np

st.write("Welcome to Streamlit demo!! ")
if st.button("Hello"):
    st.write("Thanks !!")
    
st.header("This si Header")
st.subheader("Tis is Sub Header")
st.text("This is teaxt")
st.markdown(""" # h1 header 
        ## H2 Header 
        ### H3 Header """)
#st.write(st)
a=[1,2,3,4,5,6,7,8,9]
arr=np.array(a)
st.write(arr)
st.write("HELOOOOOOSSS")

di={
    "Name": "Sunil",
    "Address": "Church",
    "Class": "MCA",
    "Gender": "Male"
    }
st.write(di)


# Load Dataset 
st.header("Read dataset Example")
data=pd.read_csv("train.csv")
st.write(data)
