import streamlit as st
from send_email import send_email

st.header("contact me ")

with st.form("contact me "):
    name = st.text_input("name")
    email = st.text_input("email")
    message = st.text_area("message")
    message = message + '\n' + email
    submit_button = st.form_submit_button("submit")
    if submit_button:
        send_email(message)
        st.info("your email was sent successfully")
