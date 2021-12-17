#!/usr/bin/env python
# coding: utf-8

# In[298]:


# Load the compiled model

import tensorflow as tf
from keras.models import load_model
load_model = tf.keras.models.load_model('model_neural')


# In[261]:


# Initiate Streamlit
import streamlit as st

col1a, col2a, col3a = st.columns(3)
col1a.image('iron.png')

st.title('AI & Real Face Detector')
st.image('brain.png')

# Define two columns for the button separation left-right
col1, col2, col3 = st.columns(3)


# In[ ]:


# Left button - AI face recognition button

import requests
from urllib.request import urlopen
from PIL import Image
import numpy as np 

if col1.button('Try somebody who doesn\'t exist'):
    # Load Image 
    response = requests.get("https://fakeface.rest/face/json")
    # response.json()['image_url'] - URL of the API-provided image
    img_fake = Image.open(urlopen(response.json()['image_url']))
    im_fake = img_fake.resize((200,200))
    col1.image(im_fake)
    im_fake = np.asarray(im_fake)
    im_fake = np.reshape(im_fake,(1,im_fake.shape[0],im_fake.shape[1],im_fake.shape[2]))

    # Make Prediction 
    prediction = load_model.predict(im_fake)
    if prediction == 1:
        col1.write('Real Face')
    else:
        col1.write('Fake Face')


# In[116]:


# Right button - Cohort face recognition button
import random

if col2.button('Try Ironhacker'):
    # Load Image 
    rand = random.randint(1,20)
    path = './test/cohort/{}.jpg'.format(rand)
    image_cohort = Image.open(path) ## Test Image Path
    im_cohort = image_cohort.resize((200,200))
    col2.image(im_cohort)
    im_cohort = np.asarray(im_cohort)
    im_cohort = np.reshape(im_cohort,(1,im_cohort.shape[0],im_cohort.shape[1],im_cohort.shape[2]))

    # Make Prediction 
    prediction_cohort = load_model.predict(im_cohort)
    if prediction_cohort == 1:
        col2.write('Real Face')
    else:
        col2.write('Fake Face')


# In[199]:


# Middle button - All cohort display

col4, col5, col6, col7 = st.columns(4)

if col3.button('Granular Ironhack check'):

# Load Image 
    for i in range(1,6):
        path = './test/cohort/{}.jpg'.format(i)
        image_cohort = Image.open(path) ## Test Image Path
        im_cohort = image_cohort.resize((200,200))
        col4.image(im_cohort)
        im_cohort = np.asarray(im_cohort)
        im_cohort = np.reshape(im_cohort,(1,im_cohort.shape[0],im_cohort.shape[1],im_cohort.shape[2]))

        # Make Prediction 
        prediction_cohort = load_model.predict(im_cohort)
        if prediction_cohort == 1:
            col4.write('Real Face')
        else:
            col4.write('Fake Face')
            
            
    for i in range(6,11):
        path = './test/cohort/{}.jpg'.format(i)
        image_cohort = Image.open(path) ## Test Image Path
        im_cohort = image_cohort.resize((200,200))
        col5.image(im_cohort)
        im_cohort = np.asarray(im_cohort)
        im_cohort = np.reshape(im_cohort,(1,im_cohort.shape[0],im_cohort.shape[1],im_cohort.shape[2]))

        # Make Prediction 
        prediction_cohort = load_model.predict(im_cohort)
        if prediction_cohort == 1:
            col5.write('Real Face')
        else:
            col5.write('Fake Face')
            
    for i in range(11,16):
        path = './test/cohort/{}.jpg'.format(i)
        image_cohort = Image.open(path) ## Test Image Path
        im_cohort = image_cohort.resize((200,200))
        col6.image(im_cohort)
        im_cohort = np.asarray(im_cohort)
        im_cohort = np.reshape(im_cohort,(1,im_cohort.shape[0],im_cohort.shape[1],im_cohort.shape[2]))

        # Make Prediction 
        prediction_cohort = load_model.predict(im_cohort)
        if prediction_cohort == 1:
            col6.write('Real Face')
        else:
            col6.write('Fake Face')
            
    for i in range(16,21):
        path = './test/cohort/{}.jpg'.format(i)
        image_cohort = Image.open(path) ## Test Image Path
        im_cohort = image_cohort.resize((200,200))
        col7.image(im_cohort)
        im_cohort = np.asarray(im_cohort)
        im_cohort = np.reshape(im_cohort,(1,im_cohort.shape[0],im_cohort.shape[1],im_cohort.shape[2]))

        # Make Prediction 
        prediction_cohort = load_model.predict(im_cohort)
        if prediction_cohort == 1:
            col7.write('Real Face')
        else:
            col7.write('Fake Face')

