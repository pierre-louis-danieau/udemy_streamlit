import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import altair as alt


def plotly():
    st.header("Display graph with plotly")
    df = px.data.tips()
    fig = px.histogram(df, x="total_bill", y="tip", color="sex",marginal="box")
    st.plotly_chart(fig)

def altair():
    st.header("Display graph with Altair")
    df = pd.DataFrame(
        np.random.randn(200, 3),
        columns=['a', 'b', 'c'])

    c = alt.Chart(df).mark_circle().encode(
        x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])

    st.altair_chart(c, use_container_width=True)

def map():
    st.header("Display a map with Open Street Map")
    df = pd.DataFrame(
        np.random.randn(200, 2) / [50, 50] + [37.76, -122.4],
        columns=['lat', 'lon'])

    st.map(df)

if __name__ == "__main__":

    st.set_page_config(
        page_title="streamlit visualization app",
        layout="centered"
    )

    st.title("Visualization tutorial for streamlit")

    plotly()

    altair()

    map()