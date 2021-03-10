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

from eda_app import run_eda_app
from mi_app import run_ml_app



def add_model():
    model = tf.kreas.models.load_model('model.h5')
    return model


def main() :
    st.title('자동차 구매 예측')
    #사이드바용 메뉴
    menu = ['DataSet','EDA','ML']
    choice = st.sidebar.selectbox("메뉴",menu)

    if choice == 'DataSet' :
        st.write("다음의 데이터 셋을 이용합니다.")
        df = pd.read_csv('Car_Purchasing_Data.csv')
        st.dataframe(df)

    elif choice == 'EDA':
        run_eda_app()

    elif choice == 'ML':
        run_ml_app()

        
    elif choice == 'Predictions' :
        model_test = model.load_model('model.h5')
        new_data = ([[0, 0.36  , 0.875 , 0.09547739, 0.48979592]])
        predicted_data = model.predict(new_data)

        st.write(predicted_data)

        

if __name__ == '__main__' :
    main()

