import streamlit as st
import plotly.express as px
from herows import *
import numpy as np
import plotly.express as px
import pandas as pd

@st.cache_data
def load_data_HEA_calculated():
    return pd.read_excel(io="Decile_data.xlsx", engine='openpyxl', sheet_name='Sheet1')

df_calcul = load_data_HEA_calculated()

@st.cache_data
def load_data_HEA_exp():
    return pd.read_excel(io="Decile_data_experimentale.xlsx", engine='openpyxl', sheet_name='Sheet1')

df_exp = load_data_HEA_exp()


@st.cache_data
def load_df_exp_equi():
    return pd.read_excel(io="df_exp_equi_decile.xlsx", engine='openpyxl', sheet_name='Sheet1')

df_exp_equi = load_df_exp_equi()



@st.cache_resource
def plot_density():
    fig = px.histogram(df_exp_equi, x='HERowS_Score', nbins=50,log_y=True ,color_discrete_sequence=['red'])




    fig.add_trace(px.histogram(df_exp, x='HERowS_Score', nbins=50 ,color_discrete_sequence=['blue'], title='Histogram of Scores',
                    log_y=True, labels={'count': 'Count (log scale)'}).data[0])

    fig.add_trace(px.histogram(df_calcul, x='HERowS_Score', nbins=50 ,color_discrete_sequence=['green'], title='Histogram of Scores',
                    log_y=True, labels={'count': 'Count (log scale)'}).data[0])
    return fig

density_plot = plot_density()

st.plotly_chart(density_plot ,use_container_width=True  ,use_container_height=True)
