from binascii import crc32
from cProfile import label
import pandas as pd
import numpy as np
import matplotlib.cm as cmArial
import streamlit as st
from urllib3 import encode_multipart_formdata
from PIL import Image
import page1
import page2
import page3
import page4
import aple 
import atl
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader

from ple import uvsor1
from ple import uvsor2

st.set_page_config(
    page_title="PL-PLE",
    page_icon="atom_symbol", 
    layout="wide",
    #initial_sidebar_state="expanded",
)

def main():
    with st.sidebar.expander("Select"):
        g = st.selectbox("Tool type", ('PLE'))

    save_dir =''

    if g == 'PLE': 
        aple.aple(save_dir)

def run():
    # ユーザーの資格情報取得
    config = []
    with open('config.yml') as file:
        config = yaml.load(file, Loader = SafeLoader)

    # 認証
    authenticator = stauth.Authenticate(
        config['credentials'],
        config['cookie']['name'],
        config['cookie']['key'],
        config['cookie']['expiry_days'],)

    with st.sidebar:
        name, authentication_status, user_name = authenticator.login("Login", "main")
        if authentication_status:
            authenticator.logout("Logout")
            st.write('Activated !!')

        elif authentication_status is False:
            st.error("Username/password is incorrect")
            st.stop()
        elif authentication_status is None:
            st.warning("Please enter your username and password")
            st.stop()

    main()

if __name__ == '__main__':
    st.write('2024/8/26  Ver.002 was coded by Chihaya Fujiwara')
    image1 = Image.open('data_control/image1.png')
    st.sidebar.image(image1)
    run()