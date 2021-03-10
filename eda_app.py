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


def run_eda_app() :
    st.subheader("EDA 화면입니다.")

    car_df = pd.read_csv('data/Car_Purchasing_Data.csv',encoding='ISO-8859-1')
    
    radio_menu = ['데이터프레임','통계치']

    selected_radio = st.radio('선택하세요.' , )
    if selected_radio == '데이터프레임':
        st.dataframe(car_df)

    elif selected_radio =='통계치':
        st.dataframe(car_df.describe())

