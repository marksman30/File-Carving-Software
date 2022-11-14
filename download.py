import streamlit as st
import os

def download(image_count):
    if image_count == 0:
        st.write("JPEG files not found")
    else:
        with st.expander('Extracted Files:',expanded=True):
            for i in range(image_count):
                file = open(f'./extracted/jpeg/out{i+1}.jpg','rb')
                out = file.read()
                st.image(out)
                st.download_button(
                    label="Download",
                    data=out,
                    file_name=f'out{i+1}.jpeg',
                )
                file.close()
                # os.remove(f'./extracted/jpeg/out{i+1}.jpg')
                