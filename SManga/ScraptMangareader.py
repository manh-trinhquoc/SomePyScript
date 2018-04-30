'''
Created on Nov 19, 2017
Check manga page for new content
@author: General
'''
import requests  # fetch link content
import bs4  # search in link content
import os  # make manage dir and file
import sys  # quit program when error
import logging  # logging error
import shelve  # save list of page to check
import webbrowser  # open link in browser
import time  # sleep


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

cur_dir = os.getcwd()
file_path = os.path.join(cur_dir,'DB','SManga')
vietNewsShelf = shelve.open(file_path)
list_manga_name = []
for value in vietNewsShelf.values():
    list_manga_name.append(''.join(value).lower())
url = 'http://www.mangareader.net'              # starting url
file_path = os.path.join(cur_dir)
os.makedirs(file_path, exist_ok=True)   # store list in ./SManga
file_path = os.path.join(cur_dir,'DB','OldLink.txt')
with open(file_path,'a+') as txt_OldLink:
    pass
txt_OldLink.close()
file_path = os.path.join(cur_dir,'DB','OldLink.txt')
with open(file_path,'r+') as txt_OldLink:
    old_links = txt_OldLink.read()
    logging.debug(str(old_links))
    old_links = old_links.split('\n')
txt_OldLink.close()
while True:
    # Download the page.
    logging.debug('Checking page %s...' % url)
    time.sleep(5)
    page_res = requests.get(url, headers = headers)
    try:
        page_res.raise_for_status()
    except Exception as exc:
        input('There was a problem: {1} \nWhile checking link: {2} \nPress any key to quit'.format(exc, url))
        sys.exit()
    page_res.encoding = 'utf-8'
    soup = bs4.BeautifulSoup(page_res.text,'html.parser')
    # The html of current mangas.
    list_element_all_manga = soup.select('tr[class="c6"]')
    # The names and links of current mangas
    for each_element in list_element_all_manga:
        soup = bs4.BeautifulSoup(str(each_element),'html.parser')
        list_element_manga = soup.select('a')
        # check manga name in data base
        manga_name = list_element_manga[0].getText().strip().lower()
        if ''.join(manga_name) not in list_manga_name:
            continue
        # Check manga link in database
        manga_link = url + list_element_manga[1].get('href')
        print('Checking manga: {}'.format(manga_name))
        if manga_link not in old_links:
            file_path = os.path.join(cur_dir,'DB','OldLink.txt')
            with open(file_path,'a+') as txt_OldLink:
                txt_OldLink.write(manga_link + '\n')
            txt_OldLink.close()
            user_command = input('Manga has new chap: {}.\n Open link Y/Default No\n'.format(manga_link))
            if user_command.lower() == 'y':
                webbrowser.open(manga_link)
        else:
            print('Manga: {} has not any new chap'.format(manga_name))
    print('All manga in {} is checked. Program end\n'.format(url))
    sys.exit()
