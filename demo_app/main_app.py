import streamlit as st
from PIL import Image
import pandas as pd
import matplotlib.pyplot as plt

st.title("demo app")
st.caption("this is a demo app")
image = Image.open("./data/EVdrGOqU0AUJ5HW.jpg")
st.image(image, caption="this is a image", width=200)