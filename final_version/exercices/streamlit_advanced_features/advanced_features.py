import streamlit as st
import numpy as np
import pandas as pd
from pandas_datareader import data as pdr
import yfinance as yf

def form():
    st.header("Streamlit Form tutorial")
    form = st.form(key='my-form')
    name = form.text_input('Enter your name')
    agree = form.checkbox('I agree')
    color = form.select_slider('Select a color of the rainbow',options=['red', 'orange', 'yellow'])
    submit = form.form_submit_button('Submit')

    if submit:
        st.subheader("Outputs")
        st.write(f'- Your name : {name}')
        st.write(f'- Are you agree : {agree}')
        st.write(f'- Your color : {color}')


def session():
    st.header("Streamlit Session tutorial")
    # Initialization
    if 'counter' not in st.session_state:
        st.session_state['counter'] = 0
    not_a_session_value = 0

    if st.button('click on me'):
        st.session_state['counter'] += 1
        not_a_session_value += 1
    
    st.write(st.session_state.counter, ' : This a session state value !')
    st.write(not_a_session_value, ' : This is not a session state value !')

@st.cache(suppress_st_warning=True)
def cache_function(ticker_option):
    st.write('The cache function is executed !!')
    st.write(f'Data price for : {ticker_option}')
    data_price = pdr.get_data_yahoo(ticker_option, start="2011-01-01")['Adj Close']
    return data_price
    



if __name__ == "__main__":

    st.set_page_config(
        page_title="streamlit advanced features",
        layout="centered"
    )
    yf.pdr_override()
    st.title("Streamlit advanced features")

    ##############################################
    form()

    session()

    st.header("Streamlit Cache function tutorial")
    ticker_option = st.selectbox('Ticker Option',('MSFT', 'AAPL', 'AMZ'))
    data_price = cache_function(ticker_option)
    st.dataframe(data_price)

    #############################################