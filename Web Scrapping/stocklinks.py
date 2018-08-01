import urllib2
from bs4 import BeautifulSoup
import string
import pandas as pd


alph = string.uppercase
pages = list(alph)
pages.append('others')
links = {}
for page in pages:
    html = urllib2.urlopen("http://www.moneycontrol.com/india/stockpricequote/"+page)
    soup = BeautifulSoup(html,'html.parser')
    table = soup.find_all('table',{'class':'pcq_tbl MT10'})[0]
    a_tags = table.find_all('a')
    if len(a_tags) > 0:
        for a in a_tags:
            company_name = a.text
            m_page_link = a.get('href')
            if company_name is not None and m_page_link is not None:
                links[company_name] = m_page_link

pop_links={}
for name, link in links.items():
    if 'nifty '.upper() in name.upper():
        pop_links[name]=link
        links.pop(name)
    elif 'bse '.upper() in name.upper():
        pop_links[name]=link
        links.pop(name)

# company_list=links.keys()
#
# company_list.sort()

if __name__ == '__main__':
    df = pd.DataFrame(links.items(), columns=['Company Name','MC Link'])

    df.to_csv('Stocklinks.csv', encoding='utf-8')

