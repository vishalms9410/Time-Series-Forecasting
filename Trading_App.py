import streamlit as st
from PIL import Image


st.set_page_config(
    page_title ="Trading_App",
    page_icon = "charts_with_downwards_trend:",
    layout ="wide"
)

st.title("Trading Guide App :bar_chart:")

st.header("We provide the greatest platform for you to collect all informations prior to investing the stocks.")
##st.image("app.png")
img = Image.open("app.png")
st.image(img, use_container_width=True)
st.markdown("## We provide the following services:")
 
st.markdown("#### :one: Stock Information")
st.write("Through this page, you can see all the information about stock.")

st.markdown("#### :two: Stock Prediction")
st.write("You can explore the predicted price for the next 30 days based on historical stock data and advanced forecasting models.")