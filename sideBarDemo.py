import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from plotly import graph_objs  as obj
import seaborn as sns

data=pd.read_csv("train.csv")

nav=st.sidebar.radio("Navigation:",["Home","Prediction","Contribute"])

if nav=="Home" :
    st.write("Home Page")
    st.image("data/Durga.jpg", width=500)
    if(st.checkbox("Show Data")):
        st.table(data)

    graph=st.selectbox("Which types of graph do you want:",
                       ["countplot","countplot-Sex","histogram","boxplot","displot"])    
    if(graph=="countplot"):
       sns.countplot(data["Survived"])
       data["Survived"].value_counts().plot(kind="bar")
       st.pyplot()
    if(graph=="countplot-Sex"):   
       sns.countplot(data["Sex"])
       data["Sex"].value_counts().plot(kind="pie")
       st.pyplot()
    if(graph=="histogram"):
        plt.hist(data["Age"],bins=5)
        st.pyplot()

    if(graph=="displot"):
        sns.boxplot(data["Age"])
        st.pyplot()
    

if nav== "Prediction":
    st.write("Predictions")

if nav== "Contribute":
    st.write("Contribute")    