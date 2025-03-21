import streamlit as st
from PIL import Image
import pandas as pd
import matplotlib.pyplot as plt

st.title("demo app")
st.caption("this is a demo app")

col1, col2 = st.columns(2)

with col1:
    st.subheader("this is a subheader")
    st.text("this is a text")

    code= '''
    import streamlit as st

    st.title("demo app")
    '''

    st.code(code, language="python")

    image = Image.open("EVdrGOqU0AUJ5HW.jpg")
    st.image(image, caption="this is a image", width=200)

    # video = open("再現性のヒント (1).mp4", "rb")
    # video_bytes = video.read()
    # st.video(video_bytes)

    with st.form(key="my_form"):
        name = st.text_input("Enter your name")
        address = st.text_input("Enter your address")
        
        age_category = st.selectbox(
            "Select your age category",
            ("Child", "Adult", "Senior")
        )

        hobby = st.multiselect(
            "Select your hobby",
            ("Reading", "Writing", "Sports", "Music")
        )

        submit_button = st.form_submit_button("Submit")
        cancel_button = st.form_submit_button("Cancel")
        if submit_button:
            st.write(f"Hello {name}!Sent to {address} and {age_category} and {hobby}")

with col2:
    df = pd.read_csv("random.csv")
    st.dataframe(df)
    st.table(df)
    st.line_chart(df)
    st.bar_chart(df["a"])

    fig, ax = plt.subplots()
    ax.plot(df["a"])
    ax.set_title("matplotlib chart")
    st.pyplot(fig)











