import streamlit as st
import requests
import base64
from Modules import BackgroundHandler
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()
# set_background
BackgroundHandler.set_background("./home/Background.webp")
def display_home(): # Task for Nguyen Dang Minh, Ninh Duy Tuan
    st.balloons()
    # Your function goes here!
    st.markdown( """ <style> .title { color: #ffc977; font-size: 3em; } </style> """, unsafe_allow_html=True)
    st.markdown('<div class="title">Welcome to Our Simplest Personality Test!</div>', unsafe_allow_html=True) 
    st.subheader("Discover your unique personality traits")

display_home()
