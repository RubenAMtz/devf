import streamlit as st
import numpy as np
import pandas as pd
import matplotlib
from matplotlib.figure import Figure
from PIL import Image
# from streamlit_lottie import st_lottie
import requests
from constants import TRAINING_SET, TESTING_SET
import io
from typing import Any

buffer = io.StringIO()

st.write("# Ruben Alvarez Martinez")
st.write("### Exploratory data analysis :sunglasses:")

pd.set_option("display.precision", 2)

df_e = pd.read_csv(TRAINING_SET)

st.write("Dataframe shape:", df_e.shape)
st.write("Dataframe column names:", df_e.columns)

# st.write(df_e.info())
