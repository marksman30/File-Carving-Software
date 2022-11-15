import streamlit as st
import os

def download(image_count,filetype):
    if image_count == 0:
        # st.write("JPEG files not found")
        pass
    else:
        print(image_count)
        with st.expander('Extracted Files:',expanded=True):
            for i in range(image_count):
                # st.write(f'File number: {i+1}')
                try:
                    file = open(f'./extracted/{filetype}/out{i+1}.{filetype}','rb')
                    out = file.read()
                    st.image(out,width=500)
                    st.download_button(
                        label="Download",
                        data=out,
                        file_name=f'out{i+1}.jpeg',
                    )
                    file.close()
                except:
                    pass
                # os.remove(f'./extracted/jpeg/out{i+1}.jpg')
                