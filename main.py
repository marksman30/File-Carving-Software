import streamlit as st
import os.path
import pathlib
from jpeg_file_carver import JPEG_FileCarver
from bmp_file_carver import BMP_FileCarver
import pandas as pd
from download import download

st.set_page_config(
    page_title="Ex-stream-ly Cool App",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded")

def num_imgs(filetype):
    n=0
    for path in pathlib.Path(f"./extracted/{filetype}/").iterdir():
        if path.is_file():
            n += 1
    return n

extract_clicked = False
menu = ["JPEG","BMP"]
image_count = 0
st.markdown('<img width=300 height=300  src="https://internetivo.com/ux/images/df/digital-forensics.gif"/> ', unsafe_allow_html=True)

st.title("""
    Welcome to JPGE ,BMP File Craver
""")
    
choice = st.sidebar.selectbox("Menu", menu)
uploaded_file = st.file_uploader("Choose a Dump file")


                
if uploaded_file is not None:
    if choice == 'JPEG':
        for path in pathlib.Path("./extracted/jpg/").iterdir():
            if path.is_file():
                image_count += 1
    
    
        image_count = num_imgs('jpg')
    
    
        download(image_count,'jpg')
        if st.button("Extract"):
        
            carver=JPEG_FileCarver(uploaded_file)
            # print(carver.carve())
            image_count = carver.carve()
            if image_count==0:
                st.write('No jpeg files found')
            else:
                choice="Download"
                download(image_count,'jpg')
    else:
            image_count=num_imgs('bmp')    
            download(image_count,'bmp')
            if st.button("Extract"):
        
                carver=BMP_FileCarver(uploaded_file)
                # print(carver.carve())
                image_count = carver.carve()
                print(image_count)
                if image_count==0:
                    st.write('No bmp files found')
                else:
                    choice="Download"
                    download(image_count,'bmp') 
else:
        image_count = num_imgs('jpg')
        for i in range(image_count):
            os.remove(f'./extracted/jpg/out{i+1}.jpg') 
        image_count = num_imgs('bmp')
        for i in range(image_count):
            os.remove(f'./extracted/bmp/out{i+1}.bmp') 