import requests, csv
from bs4 import BeautifulSoup
import pandas as pd
# variables for columns
prices=[]
names=[]
changes=[]
percentChanges=[]
marketCaps=[]
marketTimes=[]
totalVolumes=[]
openInterests=[]

url = "https://in.finance.yahoo.com/commodities"
r= requests.get(url)
data=r.text
soup=BeautifulSoup(data)
