import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

st.write("Ploting Example")
data=pd.DataFrame(
    np.random.randn(100,3),
    columns=["A","B","C"]
)
st.title("Line Chart")
st.line_chart(data)

st.title("Area Chart")
st.area_chart(data)

st.title("Bar Chart")
st.bar_chart(data)

plt.title("Scatter plot")
plt.scatter(data["A"],data["B"])
st.pyplot()

st.title("Map")
#st.bokeh_chart(data)
st.map()
st.title("Image Display")
st.image("data/Durga.JPG",width=500)

st.title("Mp3 Audio")
st.audio("data/mp3.MP3")

st.title("Mp4 Video")
st.video("data/Mp4.MP4")

st.title("Video from any Youtube")
st.video("https://www.youtube.com/watch?v=UN4DaSAZel4&list=PLuU3eVwK0I9PT48ZBYAHdKPFazhXg76h5&index=1&pp=iAQB")