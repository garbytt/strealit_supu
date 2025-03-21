import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# スクリプトの絶対パスを取得
current_file_path = os.path.abspath(__file__)

# スクリプトがあるディレクトリのパスを取得
current_directory = os.path.dirname(current_file_path)

# 目的のファイルへの相対パスを作成
target_file_path = os.path.join(current_directory, 'random.csv')

df = pd.read_csv(target_file_path)
st.dataframe(df)
st.table(df)
st.line_chart(df)
st.bar_chart(df["a"])

fig, ax = plt.subplots()
ax.plot(df["a"])
ax.set_title("matplotlib chart")
st.pyplot(fig)