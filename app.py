import streamlit as st
import pandas as pd
import numpy as np
import sys
import os

with st.sidebar:
    upload=st.file_uploader("upload the file")

if upload is not None:
    df=pd.read_csv(upload)
    st.dataframe(df.head())


