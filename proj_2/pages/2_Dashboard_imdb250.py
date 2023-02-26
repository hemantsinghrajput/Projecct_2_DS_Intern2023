import streamlit as st
from matplotlib import image
import os
import pandas as pd
import plotly.express as px
import numpy as np


st.title("Dashboard - IMDB 250 Data")

# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")

IMAGE_PATH = os.path.join(dir_of_interest, "images", "imdb.png")
DATA_PATH = os.path.join(dir_of_interest, "data", "imdb250.csv")

img = image.imread(IMAGE_PATH)
st.image(img)


df = pd.read_csv(DATA_PATH)
st.dataframe(df)

species = st.selectbox("Select the rating:", df['rating'].unique())

col1, col2 = st.columns(2)

fig_1 = px.histogram(df[df['rating'] == species], x="budget", y="year")
col1.plotly_chart(fig_1, use_container_width=True)

fig_2 = px.histogram(df[df['rating'] == species],x="budget", y="year")
col2.plotly_chart(fig_2, use_container_width=True)

col1, col2 = st.columns(2)

fig_11 = px.scatter(df, x="year", y="budget", color="rating")
col1.plotly_chart(fig_11, use_container_width=True)

fig_21 = px.bar(df, x="year", y="budget", color="rating")
col2.plotly_chart(fig_21, use_container_width=True)
st.subheader("Map")
df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(df)

st.header("Thank you :yellow_heart:")
