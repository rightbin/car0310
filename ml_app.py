import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
from datetime import datetime
from PIL import Image,ImageFilter,ImageEnhance
import h5py
import tensorflow.keras
from tensorflow.keras.models import model_from_json
from tensorflow.keras.callbacks import ModelCheckpoint
from tensorflow.keras.callbacks import CSVLogger
import pickle 

def run_ml_app():
    st.subheader('Machine learning')

    model =tensorflow.keras.models.load_model('data/car_ai.h5')
    
    new_data = np.array([0, 0.36  , 0.875 , 0.09547739, 0.48979592])
    
    new_data = new_data.reshape(1,-1)
    
    sc_X = joblib.load('data/sc_x.pkl')

    predicted_data = model.predict(new_data)

    st.write(predicted_data[0][0])
    
    sc_X = joblib.load('data/sc_y.pkl')

    y_pred_original sc_y.inverse_transform(predicted_data)


#pip install scikit-learn==0.23.2


