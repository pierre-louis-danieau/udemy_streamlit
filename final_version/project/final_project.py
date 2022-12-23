import streamlit as st
import pandas as pd
from pandas_datareader import data as pdr
import plotly.express as px
import numpy as np
from PIL import Image
import yfinance as yf

def parameter(df_sp,sector_default_val,cap_default_val):
    
    #### SECTOR #####
    sector_default = [sector_default_val]
    sector_values = sector_default + list(df_sp.sector.unique())
    option_sector = st.sidebar.selectbox("Sector",sector_values,index = 0)
    #### SECTOR #####

    #### MARKET CAP #####
    cap_value_default = [cap_default_val]
    cap_value_list = cap_value_default + ['Small', 'Medium', 'Large']
    cap_value = st.sidebar.selectbox('Company capitalization',cap_value_list, index = 0)
    #### MARKET CAP #####

    #### DIVIDEND #####
    dividend_value = st.sidebar.slider('Dividend rate between than (%) : ', 0.0, 10.0, value = (0.0,10.0))
    #### DIVIDEND #####

    #### PROFIT #####
    min_profit_value,max_profit_value = float(df_sp['profitMargins_%'].min()),float(df_sp['profitMargins_%'].max())
    profit_value = st.sidebar.slider('Profit margin rate greater than (%): ',min_profit_value,max_profit_value, value = min_profit_value, step = 10.0)
    #### PROFIT #####

    return option_sector, dividend_value, profit_value, cap_value

@st.cache
def read_data():
    path_data = 'final_version/project/s&p500.csv' 
    df_sp = pd.read_csv(path_data)
    return df_sp


def company_price(df_sp,option_company):
    if option_company != None:
        ticker_company = df_sp.loc[df_sp['name'] == option_company,'ticker'].values[0]
        data_price = pdr.get_data_yahoo(ticker_company, start="2011-12-31", end="2021-12-31")['Adj Close']
        data_price = data_price.reset_index(drop = False)
        data_price.columns = ['ds','y']
        return data_price

    return None

def filtering(df_sp,sector_default_val,cap_default_val,option_sector,dividend_value,profit_value,cap_value):

    #### DIVIDEND FILTERING ####
    df_sp = df_sp[
        (df_sp['dividendYield_%'] >= dividend_value[0])
        &
        (df_sp['dividendYield_%'] <= dividend_value[1])
    ]

    #### PROFIT FILTERING ####
    df_sp = df_sp[
        (df_sp['profitMargins_%'] >= profit_value)
    ]

    #### SECTOR FILTERING ####
    if option_sector != sector_default_val:
        df_sp = df_sp[(df_sp['sector'] == option_sector)]

    #### CAP MARKET FILTERING ####
    if cap_value != cap_default_val :
        if cap_value == 'Small':
            df_sp = df_sp[
            (df_sp['marketCap'] >= 0)
            &
            (df_sp['marketCap'] <= 20e9)
            ]
        
        elif cap_value == 'Medium':
            df_sp = df_sp[
            (df_sp['marketCap'] >= 20e9)
            &
            (df_sp['marketCap'] <= 100e9)
            ]

        elif cap_value == 'Large':
            df_sp = df_sp[
            (df_sp['marketCap'] >= 100e9)
            ]

    return df_sp


def show_stock_price(data_price):
    fig = px.line(data_price,x="ds", y="y", title='10 years Stock Price ')
    fig.update_xaxes(title_text='Date')
    fig.update_yaxes(title_text='Stock price')
    st.plotly_chart(fig)


def metrics(data_price):
    stock_price_2012 = data_price['y'].values[0] #Take the first value (In most case it is 3 jan. 2012)
    stock_price_2022 = data_price['y'].values[-1] #Take the last value (In most case, it is 31 dec. 2021)
    performance = np.around((stock_price_2022/stock_price_2012 - 1)*100,2)
    return stock_price_2022,performance


########################################### MAIN ###########################################################
############################################################################################################
if __name__ == "__main__":

    ####### PAGE CONFIG ###########################
    st.set_page_config(
    page_title="udemy_project_screener",
    page_icon="📈",
    initial_sidebar_state="expanded",
    )
    
    st.title('S&P500 Screener & Stock Analysis')
    st.sidebar.title('Search criteria')

    image = Image.open('final_version/project/stock.jpeg')
    yf.pdr_override()
    _, col_image_2,_ = st.columns([1,3,1])
    with col_image_2:
        st.image(image, caption='@austindistel')

    ############ READ DATA ##########################
    df_sp = read_data()


    ############ DATAFRAME FILTERING ################
    sector_default_val = 'All'
    cap_default_val = 'All'
    option_sector,dividend_value, profit_value, cap_value = parameter(df_sp,sector_default_val,cap_default_val)
    df_sp = filtering(df_sp,sector_default_val,cap_default_val,option_sector,dividend_value,profit_value,cap_value)

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


    ############# PART 2 - COMPANY SELECTION #####################
    st.subheader('Part 2 - Choose a company')
    option_company = st.selectbox("Choose a company from the following list :",df_sp.name.unique())


    ############# PART 3 - STOCK PREDICTION #####################
    st.subheader('Part 3 - {} Stock Analysis'.format(option_company))
    data_price = company_price(df_sp, option_company)

    ############ SHOW STOCK PRICE & PREDICTION ##############
    show_stock_price(data_price)
    stock_price_2022, performance = metrics(data_price)


    col_prediction_1,col_prediction_2 = st.columns([1,2])
    with col_prediction_1:
        st.metric(label="Stock price 31 dec. 2021", value=str(np.around(stock_price_2022,2)), delta=str(performance)+ ' %')
        st.write('*Compared to 31 dec. 2011*')

    with col_prediction_2:
        with st.expander("Prediction explanation",expanded=True):
            st.write("""
                The graph above shows the evolution of the selected stock price between 31st dec. 2011 and 31 dec. 2021.
                The indicator on the left is the stock price value in 31st dec. 2021 for the selected company and its evolution between 31st dec. 2011 and 31st dec. 2021.
                
                ⚠️⚠️ Theses value are computed based on what the Yahoo Finance API returns !
            """)


    ######################################## END #######################################################################
    ####################################################################################################################

