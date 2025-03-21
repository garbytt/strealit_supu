import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("./data/random.csv")
st.dataframe(df)
st.table(df)
st.line_chart(df)
st.bar_chart(df["a"])

fig, ax = plt.subplots()
ax.plot(df["a"])
ax.set_title("matplotlib chart")
st.pyplot(fig)