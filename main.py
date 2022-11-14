import streamlit as st
import os.path
import pathlib
from jpeg_file_carver import JPEG_FileCarver
st.set_page_config(
    page_title="Ex-stream-ly Cool App",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded")
st.markdown('<img src="https://internetivo.com/ux/images/df/digital-forensics.gif"/> ', unsafe_allow_html=True)

st.title("""
Welcome to JPGE ,BMP File Craver
""")

uploaded_file = st.file_uploader("Choose a Dump file")
# print(uploaded_file)
if uploaded_file is not None:
    if st.button("Extract"):
        carver=JPEG_FileCarver(uploaded_file)
        print(carver.carve())