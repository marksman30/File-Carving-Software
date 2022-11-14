import streamlit as st
import os.path
import pathlib
from jpeg_file_carver import JPEG_FileCarver
import pandas as pd
from download import download

st.set_page_config(
    page_title="Ex-stream-ly Cool App",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded")

def num_imgs():
    n=0
    for path in pathlib.Path("./extracted/jpeg/").iterdir():
        if path.is_file():
            n += 1
    return n

extract_clicked = False
menu = ["JPEG","BMP"]
image_count = 0
for path in pathlib.Path("./extracted/jpeg/").iterdir():
    if path.is_file():
        image_count += 1
choice = st.sidebar.selectbox("Menu", menu)

if choice == 'JPEG':
    st.markdown('<img src="https://internetivo.com/ux/images/df/digital-forensics.gif"/> ', unsafe_allow_html=True)

    st.title("""
    Welcome to JPGE ,BMP File Craver
""")
    uploaded_file = st.file_uploader("Choose a Dump file")
    image_count = num_imgs()
    download(image_count)
    if uploaded_file is not None:
        if st.button("Extract"):
        
            carver=JPEG_FileCarver(uploaded_file)
            # print(carver.carve())
            image_count,extracted = carver.carve()
            if image_count==0:
                st.write('No jpeg files found')
            else:
                choice="Download"
                download(image_count)
    else:
            image_count = num_imgs()
            for i in range(image_count):
                os.remove(f'./extracted/jpeg/out{i+1}.jpg') 
else:
    pass
                    