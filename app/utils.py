import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

def load_data():
    # Replace this with your own CSV path
    return pd.read_csv("data/solar_data.csv")

def boxplot_ghi(data):
    fig, ax = plt.subplots()
    sns.boxplot(y=data['GHI'], ax=ax)
    st.pyplot(fig)

def histogram_ghi(data):
    fig, ax = plt.subplots()
    sns.histplot(data['GHI'], kde=True, ax=ax)
    st.pyplot(fig)

def get_top_regions(data, top_n=5):
    return data.groupby("region")["GHI"].mean().sort_values(ascending=False).head(top_n).reset_index()
