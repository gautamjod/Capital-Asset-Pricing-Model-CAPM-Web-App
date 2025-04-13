#importing required Librabies
import streamlit as st
import pandas as pd
import yfinance as fyf
import pandas_datareader.data as web
import datetime 
import capm_func

#setting page
st.set_page_config(page_title="CAPM",page_icon="chart_with_upwards_trend",layout="wide")
st.title("Capital Asset Pricing Model")

#getting input
col1,col2 = st.columns([1,1])
with col1:
    stock_list = st.multiselect("Choose 4 Stocks" ,('TSLA','AAPL','NFLX','MSFT','MGM','AMZN','NVDA','GOOGL'),['TSLA','AAPL','AMZN','GOOGL'])
with col2:  
    years=st.number_input("Number Of years",1,10)
    
st.markdown("---")
#download SP500 data

try:
    end = datetime.date.today()
    start = datetime.date(datetime.date.today().year-years,datetime.date.today().month,datetime.date.today().day)

    sp500 = web.DataReader(['SP500'],'fred',start,end)
    print(sp500.info())

    stock_df=pd.DataFrame()

    for stocks in stock_list:
        data=fyf.download(stocks,period=f'{years}y')
        stock_df[f'{stocks}']=data['Close']
        

    stock_df.reset_index(inplace=True)
    sp500.reset_index(inplace=True)
    sp500.rename(columns={'DATE' : 'Date'},inplace=True)

    stock_df=pd.merge(stock_df,sp500,on="Date",how='inner')

    stock_df['Date']=stock_df['Date'].dt.strftime('%d-%m-%Y')

    col1,col2=st.columns([1,1])
    st.markdown("---")

    with col1 :
        st.markdown("### DataFrame Head")
        st.dataframe(stock_df.head(),use_container_width=True)
    with col2 :
        st.markdown("### DataFrame Tail")
        st.dataframe(stock_df.tail(),use_container_width=True)
    
    col1,col2=st.columns([1,1])
    
    with col1:
        st.markdown("### Price of all Stocks")
        st.plotly_chart(capm_func._plots(stock_df))
    with col2 :
        st.markdown("### Compaing Stock Volatility")
        st.plotly_chart(capm_func._plots(capm_func.normal(stock_df)))
        
   
    stock_daily_return=capm_func.daily_return(stock_df)
    print(stock_daily_return.head())

    beta={}
    alpha={}

    for i in stock_daily_return:
        if i!='Date' and i!='SP500':
            b,a=capm_func._beta(stock_daily_return,i)
            beta[i]=b
            alpha[i]=a
    print(beta,alpha)

    beta_df=pd.DataFrame(columns=['Stock','Beta'])
    beta_df['Stock']=beta.keys()
    beta_df['Beta']=[str(round(i,2)) for i in beta.values()]
    st.markdown("---")
    col1,col2=st.columns([1,1])
    with col1:
        st.markdown("### Calculated Beta Values")
        st.dataframe(beta_df,use_container_width=True)

    rf=0
    rm=stock_daily_return['SP500'].mean()*252

    return_df = pd.DataFrame()

    return_value=[]

    for stock ,value in beta.items():
        return_value.append(str((round(rf+(value*(rf-rm)),2))))


    return_df['Stock']=stock_list
    return_df['Return Value']=return_value

    with col2:
        st.markdown("### Caculated Return using CAPM")
        st.dataframe(return_df,use_container_width=True)
except:
    st.write("Please Select Valid Options")