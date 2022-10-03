import streamlit as st
import pandas as pd
from pandas_datareader import data as pdr
import plotly.express as px
import numpy as np
from PIL import Image


def read_data():
    path_data = 'final_version/project/s&p500.csv'
    df_sp = pd.read_csv(path_data)
    return df_sp
    

if __name__ == "__main__":

    ####### PAGE CONFIG ###########################
    st.set_page_config(
    page_title="udemy_project_screener",
    page_icon="📈",
    initial_sidebar_state="expanded",
    )

    st.title('S&P500 Screener & Stock Prediction')
    st.sidebar.title('Search criteria')

    image = Image.open('final_version/project/stock.jpeg')
    _, col_image_2,_ = st.columns([1,3,1])
    with col_image_2:
        st.image(image, caption='@austindistel')

    ############ READ DATA ##########################
    df_sp = read_data()


    ############# PART 1 - SCREENER #####################
    st.subheader('Part 1 - S&P 500 Screener')
    with st.expander("Part 1 explanation",expanded=False):
        st.write("""
            In the table below, you will find most of the companies in the S&P500 (stock market index of the 500 largest American companies) with certain criteria such as :
                
                - The name of the company
                - The sector of activity
                - Market capitalization
                - Dividend payout percentage (dividend/stock price)
                - The company's profit margin in percentage
            
            ⚠️ This data is scrapped in real time from the yahoo finance API. ⚠️

            ℹ️ You can filter / search for a company with the filters on the left. ℹ️
        """)
    st.write('Number of companies found : ', len(df_sp))
    st.dataframe(df_sp.iloc[:,1:])

