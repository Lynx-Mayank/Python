from bs4 import BeautifulSoup as b

#pip install requests

import requests as r
import pandas as p

myURL= 'https://www.skysports.com/f1/standings'
downloadURL=r.get(myURL, headers={'User Agent':"test"})

soup= b(downloadURL.text, "html.parser")

fullTable = soup.select('tbody')[0]

driver = fullTable.select('a span')


tableRows = []


for d in driver:
    tableRows.append(str(d).replace('<span class="standing-table_cell--name-text">', '').replace('</span>', '').strip())

df = p.DataFrame (tableRows, columns=['DriverName'])