import streamlit as st
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