import streamlit as st
from PIL import Image, ImageOps
from playsound3 import playsound
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MUSIC_PATH = os.path.join(BASE_DIR, "fah.mp3")


with st.expander("click your happy picture"):
    camera=st.camera_input("Camera")


print(camera)

if camera:
    img=Image.open(camera)

    gray_img=img.convert("L")
    colorized = ImageOps.colorize(gray_img, black="blue", white="yellow")

    st.image(gray_img)
    playsound("fah.mp3")