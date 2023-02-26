import streamlit as st
import os
from matplotlib import image

st.title(":red[Innomatics] Data App")
st.header(":blue[Hemant Rajput]- Data Science Enthusiast")
#st.snow()
img = image.imread('./resources/images/hemant.jpg')

btn_click = st.button("Click Me! to see my Dashboard")

st.text("I'm a front end react developer and a Data Scientist Enthusiast with a Intermediate knowledge of Machine Learning.")

if btn_click == True:
    st.subheader("Welcome to my Dashboard :smile:")
    st.balloons()
    st.image(img)
    st.header("Thank you :yellow_heart:")
