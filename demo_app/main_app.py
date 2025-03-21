import streamlit as st
from PIL import Image
import os

# スクリプトの絶対パスを取得
current_file_path = os.path.abspath(__file__)

# スクリプトがあるディレクトリのパスを取得
current_directory = os.path.dirname(current_file_path)

# 目的のファイルへの相対パスを作成
target_file_path = os.path.join(current_directory, 'EVdrGOqU0AUJ5HW.jpg')

st.title("demo app")
st.caption("this is a demo app")
image = Image.open(target_file_path)
st.image(image, caption="this is a image", width=200)