#!/usr/bin/env python3
import requests
import os
from bs4 import BeautifulSoup


link_horizon = 'https://store.playstation.com/ru-ru/product/EP9000-CUSA01021_00-HRZ000000000DLC1'
link_gta5 = 'https://store.playstation.com/ru-ru/product/EP1004-CUSA00411_00-PREMIUMPACKOG001'
BASE_URL = 'https://api.telegram.org/'

TOKEN = os.environ.get('TOKEN')
message = ''


def send_message(message):

    req = requests.get(f'{BASE_URL}{TOKEN}/')


r = requests.get(link_horizon)
b = BeautifulSoup(r.text, 'html.parser')

price1 = b.select('.price-display__price')
price2 = b.select('.price')

if not price2:
    message = 'NOT DISCOUNT\nPrice: {0}'.format(price1[0].text)

else:
    message = 'DISCOUNT!\nOld price is: {0}.\n Discount price is: {1}'.format(price2[0].text, price1[0].text)


if __name__ == '__main__':
    send_message(message)
