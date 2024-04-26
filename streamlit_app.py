import pandas as pd
import streamlit as st

df = pd.read_csv('https://github.com/WilliamSchultz/steamlit_app/blob/main/allb.csv?raw=true')

df = df[['domain', 'title', 'category', 'brand', 'url', 'items', 'rev']]

st.dataframe(df)
