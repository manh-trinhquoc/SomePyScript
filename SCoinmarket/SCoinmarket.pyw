'''
Created on Nov 23, 2017
Srcapt Coinmarket for price-push notification when price exceed a value
@author: General
'''

import requests  # fetch link content
import bs4  # search in link content
import os  # make manage dir and file
import sys  # quit program when error
import logging  # logging error
import shelve  # save high value and low value
#import webbrowser  # open link in browser
import time  # make script sleep for seconds


logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.DEBUG)
logging.debug('Start of code')

# Modify header for requests
headers = {
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Language':'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,ko;q=0.4,ja;q=0.3,zu;q=0.2',
    'Connection':'keep-alive',
    'Accept-Encoding':'gzip, deflate, br',
    }

def exec_full(filepath,list_variable):
    import os
    global_namespace = {
        "__file__": filepath,
        "__name__": "__main__",
        "each_coin": list_variable[0],
        "price":list_variable[1]
    }
    with open(filepath, 'rb') as file:
        exec(compile(file.read(), filepath, 'exec'), global_namespace)

# thresole level
bitcoin_hight = 20000
bitcoin_low = 10000
ether_hight = 1500
ether_low = 900
iota_hight = 6
iota_low = 3

url = 'https://coinmarketcap.com/'
while True:
    # Show 1 time and quit
    if sys.argv[len(sys.argv)-1] == 'now':
        show_now = True
    # Show after sleep and continue
    else:
        show_now = False
        time.sleep(3)
    # Download the page.
    print('Checking coinmarket price....')
    time.sleep(5)
    page_res = requests.get(url, headers = headers)
    try:
        page_res.raise_for_status()
    except Exception as exc:
        input('There was a problem: {1} \nWhile checking link: {2} \nPress any key to quit'.format(exc, url))
        sys.exit()
    page_res.encoding = 'utf-8'
    soup = bs4.BeautifulSoup(page_res.text,'html.parser')
    # TODO: refactor
    list_coin_name = ['id-bitcoin', 'id-ethereum', 'id-iota']
    for each_coin in list_coin_name:
        list_element_id_coin_name = soup.select('tr[id="{}"]'.format(each_coin))
        # The links of current result
        for each_element in list_element_id_coin_name:
            soup_id_coin = bs4.BeautifulSoup(str(each_element),'html.parser')
            list_element_price_tag = soup_id_coin.select('a[class="price"]')
            price = list_element_price_tag[0].get('data-usd')
            logging.debug('{} price is: {}'.format(each_coin, price))
            # TODO: reafactor
            float_price = float(price)
            if each_coin == 'id-bitcoin':
                if float_price > bitcoin_hight or float_price < bitcoin_low:
                    os.system('python printConsole.py {} {}'.format(each_coin, price))
                    #exec_full('/home/manh/git/SomePyScript/SCoinmarket/printConsole.py',[each_coin,price])
            elif each_coin == 'id-ethereum':
                if float_price > ether_hight or float_price < ether_low:
                    #exec_full('/home/manh/git/SomePyScript/SCoinmarket/printConsole.py',[each_coin,price])
                    os.system('python printConsole.py {} {}'.format(each_coin, price))
            elif each_coin == 'id-iota':
                if float_price > iota_hight or float_price < iota_low:
                    # exec_full('/home/manh/git/SomePyScript/SCoinmarket/printConsole.py',[each_coin,price])
                    os.system('python printConsole.py {} {}'.format(each_coin, price))
            if show_now == True:
                #exec_full('/home/manh/git/SomePyScript/SCoinmarket/printConsole.py',[each_coin,price])
                os.system('python printConsole.py {} {}'.format(each_coin, price))
    if show_now == True:
        sys.exit()
print("program end")
