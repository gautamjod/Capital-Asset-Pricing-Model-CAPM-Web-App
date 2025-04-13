import plotly.express as px
import numpy as np


def _plots(df):
    fig=px.line()
    for i in df.columns[1:]:
        fig.add_scatter(x=df['Date'],y=df[i],name=i)
    fig.update_layout(width=450,margin=dict(l=20,r=20,t=50,b=20),legend=dict(orientation='h',yanchor='bottom',y=1.02,xanchor='right',x=1) )
    return fig

def normal(df_2):
    df=df_2.copy()
    for i in df.columns[1:]:
        df[i]=df[i]/df[i][0]
    return df

def daily_return(df):
    df_3=df.copy()
    for i in df.columns[1:]:
        for j in range(1,len(df)):
            df_3[i][j]=((df[i][j]-df[i][j-1])/df[i][j-1])*100
        df_3[i][0]=0
    return df_3


def _beta(stocks_daily_return,stocks):
    rm=stocks_daily_return['SP500'].mean()
    
    b,a=np.polyfit(stocks_daily_return['SP500'],stocks_daily_return[stocks],1)   
    return b,a