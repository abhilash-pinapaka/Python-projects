import urllib2
from bs4 import BeautifulSoup
import pandas as pd
import logging


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler('stocksdata2.log')
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(name)s - %(levelname)s -%(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
MC_stocks = pd.read_csv('Stocklinks.csv')
stock_details = {}

for i in range(4000,6000):
    stock_data = {'company_name': MC_stocks.loc()[i][1]}
    market_details = {}
    try:
        url = MC_stocks.loc()[i][2]
        html_data = urllib2.urlopen(url)
        soup = BeautifulSoup(html_data, 'html.parser')
        index_data = soup.find_all('div', {'id': 'content_full'})
        market_data = soup.find_all('div', {'id': 'mktdet_1'})
        if len(index_data) > 0:
            bse_data = index_data[0].find_all('div', {'id': 'content_bse'})
            nse_data = index_data[0].find_all('div', {'id': 'content_nse'})

            if 'not listed on BSE' not in bse_data[0].text and len(bse_data) > 0:
                bse_LH=None
                bse_price = bse_data[0].find_all('div', {'id': 'Bse_Prc_tick_div'})
                if len(bse_price) > 0:
                    for price in bse_price:
                        stock_data['bse_price'] = price.text
                    for fr in bse_data[0].find_all('div', {'class': 'FR'}):
                        if len(fr.get('class')) == 1:
                            bse_LH = fr
                            tmp = bse_LH.text.split('\n\n\n')
                            low, high = tmp[1].split()[-2:]
                            stock_data['bse_52wk_low'] = low
                            stock_data['bse_52wk_high'] = high
                else:
                    stock_data['bse_price'] = 'NA'
                    stock_data['bse_52wk_low'] = 'NA'
                    stock_data['bse_52wk_high'] = 'NA'

            else:
                stock_data['bse_price'] = 'NA'
                stock_data['bse_52wk_low'] = 'NA'
                stock_data['bse_52wk_high'] = 'NA'

            if 'not listed on NSE' not in nse_data[0].text and len(nse_data) > 0:
                nse_LH=None
                nse_price = nse_data[0].find_all('div', {'id': 'Nse_Prc_tick_div'})
                if len(nse_price) > 0:
                    for price in nse_price:
                        stock_data['nse_price'] = price.text

                    for fr in nse_data[0].find_all('div', {'class': 'FR'}):
                        if len(fr.get('class')) == 1:
                            nse_LH = fr
                            tmp = nse_LH.text.split('\n\n\n')
                            low, high = tmp[1].split()[-2:]
                            stock_data['nse_52wk_low'] = low
                            stock_data['nse_52wk_high'] = high
                else:
                    stock_data['nse_price'] = 'NA'
                    stock_data['nse_52wk_low'] = 'NA'
                    stock_data['nse_52wk_high'] = 'NA'
            else:
                stock_data['nse_price'] = 'NA'
                stock_data['nse_52wk_low'] = 'NA'
                stock_data['nse_52wk_high'] = 'NA'
        if len(market_data) > 0:
            innerHtml=market_data[0].find_all('div', {'class': 'PA7 brdb'})
            if len(innerHtml) > 0:
                for dt in innerHtml:
                    a = dt.text.strip().split('\n')
                    if len(a) > 1:
                        market_details[a[0]] = a[1]
                    else:
                        market_details[a[0]] = 'NA'
    except Exception as err:
        logger.info('%s - exception %s', i, err)
    stock_data.update(market_details)
    logger.info("%s - Records %s",i, stock_data['company_name'])

    stock_details[MC_stocks.loc()[i][1]] = stock_data
    del stock_data

#print stock_details
df_stocks=pd.DataFrame(stock_details)
pd.DataFrame(df_stocks.T).to_csv('StockData2.csv', encoding='utf-8')