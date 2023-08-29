import streamlit as st
import plotly.express as px
from herows import *
import numpy as np
import plotly.express as px
import pandas as pd

st.set_page_config(page_title="HEAowS", 
                   page_icon=":bar_chart:",
                   layout="wide")

@st.cache_data
def load_data_HEA_calculated():
    return pd.read_excel(io="finale.xlsx", engine='openpyxl', sheet_name='Sheet1')

df_calcul = load_data_HEA_calculated()

selected_categories = st.multiselect(
        "Select Categories",
        df_calcul['ETAT'].unique(),
        default=['equimolat experimental data', 'experimental data']
    )
    
    # Filter data based on selected categories
filtered_data = df_calcul[df_calcul['ETAT'].isin(selected_categories)]

#@st.cache_resource
def plot_density():
    fig = px.histogram(filtered_data, x="HERowS_Score", color="ETAT", log_y=True)
    return fig

density_plot = plot_density()

st.plotly_chart(density_plot ,use_container_width=True  ,use_container_height=True)
