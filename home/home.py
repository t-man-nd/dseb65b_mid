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
   st.markdown( """ <style> .title { background-color: #FFE4E1; font-size: 3em; padding: 0.5em; border-radius: 0.25em; } </style> """, unsafe_allow_html=True ) 
   st.markdown('<div class="title">WELCOME TO OUR SIMPLEST PERSONALITY CHECK</div>', unsafe_allow_html=True)
   if st.button("Start Your Personality Test"): 
      st.write("Starting the personality test...")

display_home()
