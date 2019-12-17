import requests
from bs4 import BeautifulSoup

link = 'https://store.playstation.com/ru-ru/product/EP9000-CUSA01021_00-HRZ000000000DLC1'

r = requests.get(link)

b = BeautifulSoup(r.text, 'html.parser')
price = b.select('.price-display__price')
print(price[0].text)

#<h3 class="price-display__price">RUB&nbsp;1.069</h3>select
