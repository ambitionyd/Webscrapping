import streamlit as st
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
import sys
st.title("Flipkart Webscrapper")
def get_data(keyword):
    flipkart_link="https://www.flipkart.com/search?q={}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
    search_link=flipkart_link.format(keyword.replace(" ",""))
    product_page=urlopen(search_link)
    product_html=product_page.read()
    product_html=BeautifulSoup(product_html,'html.parser')
    product_links=product_html.find_all('a',{'class','_1fQZEK'})
    ans=["https://www.flipkart.com"+link['href'] for link in product_links]
    comments=[]
    username=[]
    for link in ans:
        page=urlopen(link)
        page=page.read()
        page_html=BeautifulSoup(page,'html.parser')
        username_list=page_html.find_all('p',{'class':"_2sc7ZR _2V5EHH"})
        username=username+[name.text for name in username_list]
        comments_list=page_html.find_all('div',{'class':'t-ZTKy'})
        comments=comments+[com.div.div.text for com in comments_list]
    df=pd.DataFrame([username,comments])
    df=df.T
    df.columns=['username','comment']
    return df
with st.spinner("loading"):
    keyword=st.text_input(label="Search on Flipkart")
    st.dataframe(get_data(keyword),width=10000)