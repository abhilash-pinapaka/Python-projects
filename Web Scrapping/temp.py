import urllib2
from bs4 import BeautifulSoup
import pandas as pd

df = pd.read_csv('StockData.csv')

#df_stk.to_csv('StockData_res.csv', encoding='utf-8')
# for row in df.iterrows():
#     if len(row) < 3:
#         print row


