import streamlit as st
from PIL import Image
import pandas as pd
import matplotlib.pyplot as plt

import os

st.write("Current Working Directory:", os.getcwd())
st.write("Files in current directory:", os.listdir("."))
st.write("Files in 'data' directory:", os.listdir("data") if os.path.exists("data") else "No 'data' directory found")

data_dir = os.path.join(os.getcwd(), "data")
image_path = os.path.join(data_dir, "EVdrGOqU0AUJ5HW.jpg")
st.write(image_path)

st.title("demo app")
st.caption("this is a demo app")
image = Image.open("./data/EVdrGOqU0AUJ5HW.jpg")
st.image(image, caption="this is a image", width=200)