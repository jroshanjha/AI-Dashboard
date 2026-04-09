import streamlit as st
import requests

API_URL = "http://localhost:8000"

st.title("🤖 AI Dashboard")

option = st.selectbox("Choose Task", ["Chat", "Image", "PDF"])

if option == "Chat":
    user_input = st.text_input("Ask something")
    if st.button("Send"):
        res = requests.post(f"{API_URL}/nlp", params={"text": user_input})
        st.write(res.json())

elif option == "Image":
    file = st.file_uploader("Upload Image")
    if file:
        res = requests.post(f"{API_URL}/image", files={"file": file})
        st.write(res.json())

elif option == "PDF":
    file = st.file_uploader("Upload PDF")
    if file:
        res = requests.post(f"{API_URL}/pdf", files={"file": file})
        st.write(res.json())