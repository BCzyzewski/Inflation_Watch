import pandas as pd
import streamlit as st
import plotly.express as px
import numpy as np


data_path = r'Inflation Data.csv'


@st.cache
def load_data():
    df = pd.read_csv(data_path)
    df['Value'].replace(':', np.nan, inplace=True)
    df['Value'] = df['Value'].astype('float')
    df['TIME'] = pd.to_datetime(df['TIME'])

    return df


data = load_data()


df_chosen = data[data['GEO'] == 'Poland']


line_chart = px.line(
    df_chosen,
    x='TIME', y='Value', title='HICP inflation rate in Poland',
    labels={
        "TIME": "Time",
        "Value": "HICP inflation (annual rate of change)"
    }
)


st.title('Inflation Watch')

st.write(line_chart)
