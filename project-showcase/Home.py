import streamlit as st
import pandas



st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")
with col2:
    st.title("Hasan Iqbal")
    content = ''' Hi I am a Devops Engineer '''
    st.info(content)

st.text("These are some apps I have built in Python")

col3, empty, col4 = st.columns([1.5,0.5,1.5])
dataFrame = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in dataFrame[1:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in dataFrame[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])   
        st.write(f"[Source Code]({row['url']})")                     

