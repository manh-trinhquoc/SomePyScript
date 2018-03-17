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
vietNewsShelf = shelve.open(os.path.join('C:\\001MyPythonScript\\SManga\\DB','SManga'))
list_manga_name = []
for value in vietNewsShelf.values():
    list_manga_name.append(''.join(value).lower())
url = 'http://truyentranhtuan.com'              # starting url
os.makedirs('C:/001MyPythonScript/SManga/DB', exist_ok=True)   # store list in ./SManga
with open('C:/001MyPythonScript/SManga/DB/OldLink.txt','a+') as txt_OldLink:
    pass
txt_OldLink.close()
with open('C:/001MyPythonScript/SManga/DB/OldLink.txt','r+') as txt_OldLink:
    old_links = txt_OldLink.read()
    logging.debug(str(old_links))
    old_links = old_links.split('\n')
txt_OldLink.close()
while True:
    # Download the page.
    logging.debug('Checking page %s...' % url)
    time.sleep(5)
    page_res = requests.get(url)
    try:
        page_res.raise_for_status()
    except Exception as exc:
        input('There was a problem: {1} \nWhile checking link: {2} \nPress any key to quit'.format(exc, url))
        sys.exit()
    #soup = bs4.BeautifulSoup(page_res.text,'html.parser')
    page_res.encoding = 'utf-8'
    soup = bs4.BeautifulSoup(page_res.text,'html.parser')  #  TODO: comment out
    # The html of current mangas.
    list_element_all_manga = soup.select('.manga-focus')
    # The names and links of current mangas
    for each_element in list_element_all_manga:
        soup = bs4.BeautifulSoup(str(each_element),'html.parser')
        list_element_manga = soup.select('a')
        manga_name = list_element_manga[0].getText().strip().lower()
        manga_name_encoded = list_element_manga[0].getText().strip().lower().encode('utf-8')  # TODO: comment out
        # check manga name in data base
        if ''.join(manga_name) not in list_manga_name:
            continue
        # Check manga link in database
        manga_link = list_element_manga[1].get('href')
        print('Checking manga: {}'.format(manga_name))
        if manga_link not in old_links:
            with open('C:/001MyPythonScript/SManga/DB/OldLink.txt','a+') as txt_OldLink:
                txt_OldLink.write(manga_link + '\n')
            txt_OldLink.close()
            user_command = input('Manga has new chap: {}.\n Open link Y/Default No\n'.format(manga_link))
            if user_command.lower() == 'y':
                webbrowser.open(manga_link)
        else:
            print('Manga: {} has not any new chap'.format(manga_name))
    print('All manga in {} is checked. Press any key to quit\n'.format(url))
    sys.exit()
