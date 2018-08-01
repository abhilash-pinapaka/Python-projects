import urllib2
from bs4 import BeautifulSoup
import stocklinks


class Stock(object):
    def __init__(self, name, stock_data=None):
        if stock_data is None:
            self.stock_data = {'company_name': name}

    def get_html(self, url):
        html_data = urllib2.urlopen(url)
        bs = BeautifulSoup(html_data, 'html.parser')
        return bs

    def get_bse_prices(self, bsoup):
        data = bsoup.find_all('div', {'id': 'content_full'})
        bse_data = data[0].find_all('div', {'id': 'content_bse'})
        if 'not listed on BSE' not in bse_data[0].text:
            for price in bse_data[0].find_all('div', {'id': 'Bse_Prc_tick_div'}):
                self.stock_data['bse_price'] = price.text
            for fr in bse_data[0].find_all('div', {'class': 'FR'}):
                if len(fr.get('class')) == 1:
                    lh = fr
            tmp = lh.text.split('\n\n\n')
            low, high = tmp[1].split()[-2:]
            self.stock_data['bse_52wk_low'] = low
            self.stock_data['bse_52wk_high'] = high
        else:
            self.stock_data['bse_price'] = 'NA'
            self.stock_data['bse_52wk_low'] = 'NA'
            self.stock_data['bse_52wk_high'] = 'NA'

    def get_nse_prices(self, bsoup):
        data = bsoup.find_all('div', {'id': 'content_full'})
        nse_data = data[0].find_all('div', {'id': 'content_nse'})
        lh = None
        low = None
        high = None
        if 'not listed on NSE' not in nse_data[0].text:
            for price in nse_data[0].find_all('div', {'id': 'Nse_Prc_tick_div'}):
                self.stock_data['nse_price'] = price.text

            for fr in nse_data[0].find_all('div', {'class': 'FR'}):
                if len(fr.get('class')) == 1:
                    lh = fr
            tmp = lh.text.split('\n\n\n')
            low, high = tmp[1].split()[-2:]
            self.stock_data['nse_52wk_low'] = low
            self.stock_data['nse_52wk_high'] = high
        else:
            self.stock_data['nse_price'] = 'NA'
            self.stock_data['nse_52wk_low'] = 'NA'
            self.stock_data['nse_52wk_high'] = 'NA'

    def get_prices(self, bsoup):
        self.get_bse_prices(bsoup)
        self.get_nse_prices(bsoup)


if __name__ == '__main__':
    stocks_dict = {}
    companies_list = stocklinks.links.keys()
    for company_name in companies_list:
        if company_name:
            url = stocklinks.links[company_name]
            stock = Stock(company_name)
            bs = stock.get_html(url)
            stock.get_prices(bs)
            stocks_dict[company_name] = stock.stock_data

    print stocks_dict
