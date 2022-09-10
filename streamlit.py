import streamlit as st
import tensorflow as tf
from tensorflow import keras
from keras.models import load_model
st.write("Hello There")
st.write(tf.__version__)
mn=load_model("C:\\Users\\sridh\\Downloads\\test2.h5")
mn.summary()


from PIL import Image
import numpy as nps

import cv2
import time

st.title("Webcam Live Feed")
run = st.checkbox('Run')
FRAME_WINDOW = st.image([])
camera = cv2.VideoCapture(0)

while run:
    _, frame = camera.read()
    image1 = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    image1_b_w = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    st.title(image1_b_w.shape)
    time.sleep(0.01)
    _, frame1 = camera.read()
    image2 = cv2.cvtColor(frame1, cv2.COLOR_BGR2RGB)
    image2_b_w = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
    absdiff = cv2.absdiff(image1_b_w,image2_b_w)
    FRAME_WINDOW.image(absdiff)

else:
    st.write('Stopped')