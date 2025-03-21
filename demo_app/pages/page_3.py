import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

st.write("Current Working Directory:", os.getcwd())
st.write("Files in current directory:", os.listdir("."))
st.write("Files in 'data' directory:", os.listdir("data") if os.path.exists("data") else "No 'data' directory found")

data_dir = os.path.join(os.getcwd(), "demo_app", "data")
csv_path = os.path.join(data_dir, "random.csv")
df = pd.read_csv(csv_path)
st.dataframe(df)
st.table(df)
st.line_chart(df)
st.bar_chart(df["a"])

fig, ax = plt.subplots()
ax.plot(df["a"])
ax.set_title("matplotlib chart")
st.pyplot(fig)