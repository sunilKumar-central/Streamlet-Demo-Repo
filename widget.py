import streamlit as st
import datetime
import pandas as pd
import matplotlib.pyplot as plt

st.title("WIDGETES EXAMPLE")



st.title("Simple Button")
st.button("Subscribe")


st.title("Simple Button Action to perform any task")
if st.button("Like"):
    st.write("Thank you !!")

st.title("Text Input")
name=st.text_input("Enter Your Name")
st.write("Name:",name)


st.title("Text  Area Input")
name=st.text_area("Enter Your Details")
st.write("Details:",name)

st.title("Checkbox")
name=st.checkbox("1st")
st.write("Details:",name)

st.title("Radio Button")
name=st.radio("Colors",['r','b','g'])
st.write("Details:",name)

st.title("Select Box")
name=st.selectbox("Colors",['r','b','g'])
st.write("Details:",name)

st.title("Slider Bar")
name=st.slider("Age",min_value=5,max_value= 100, step=2)
st.write("Details:",name)

st.title("Date")
d = st.date_input("When's your birthday", datetime.date(1989, 11, 13))
st.write("Your birthday is:", d)
st.title("Time")
name=st.time_input("Time",datetime.time())
st.write("Details:",name)

st.title("File Uploader")
file=st.file_uploader("Select File")
st.write("Details:",file)

plt.savefig("/data/study.JPG")