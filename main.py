from binascii import crc32
from cProfile import label
from distutils.command.build_scripts import first_line_re
import pandas as pd
import numpy as np
import matplotlib.cm as cmArial
import streamlit as st


st.set_page_config(
    layout="wide",
    initial_sidebar_state="expanded",
)


from urllib3 import encode_multipart_formdata
from PIL import Image
import page1
import page2
import page3
import page4
import aple 
import atl


from ple import uvsor1
from ple import uvsor2


def main():
    st.write('2024/8/26  Ver.002 coded by Chihaya Fujiwara')

    image1 = Image.open('data_control/image1.png')
    st.sidebar.image(image1)

    with st.sidebar.expander("Select"):
        g = st.selectbox("Tool type", ('PLE'))

    save_dir =''

    if g == 'PLE': 
        aple.aple(save_dir)
    

if __name__ == '__main__':
    main()
    
