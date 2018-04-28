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
vietNewsShelf = shelve.open(os.path.join('C:\\001MyPythonScript\\src\\SNewsSearch','SNewsSearch'))
list_keywords = []
for value in vietNewsShelf.values():
    list_keywords.append(''.join(value).lower())
url = 'https://timkiem.vnexpress.net/?q='              # starting url
os.makedirs('C:/001MyPythonScript/src/SNewsSearch', exist_ok=True)   # store list in ./SManga
with open('C:/001MyPythonScript/src/SNewsSearch/OldLink.txt','a+') as txt_OldLink:
    pass
txt_OldLink.close()
with open('C:/001MyPythonScript/src/SNewsSearch/OldLink.txt','r+') as txt_OldLink:
    old_links = txt_OldLink.read()
    logging.debug(str(old_links))
    old_links = old_links.split('\n')
txt_OldLink.close()
for each_keyword in list_keywords:
    # Download the page.
    print('Checking vnexpress key word: {}...'.format(each_keyword))
    #webbrowser.open(url + each_keyword)  # TODO: comment out
    time.sleep(5)
    page_res = requests.get(url + each_keyword)
    try:
        page_res.raise_for_status()
    except Exception as exc:
        input('There was a problem: {1} \nWhile checking link: {2} \nPress any key to quit'.format(exc, url))
        sys.exit()
    page_res.encoding = 'utf-8'
    soup = bs4.BeautifulSoup(page_res.text,'html.parser')
    # The html of all search results.
    list_element_all_result = soup.select('div[class="title_news"]')
    # The links of current result
    for each_element in list_element_all_result:
        soup = bs4.BeautifulSoup(str(each_element),'html.parser')
        list_element_chap = soup.select('a')
        # Check link in database
        result_link = list_element_chap[0].get('href')
        if result_link not in old_links:
            with open('C:/001MyPythonScript/src/SNewsSearch/OldLink.txt','a+') as txt_OldLink:
                txt_OldLink.write(result_link + '\n')
            txt_OldLink.close()
            user_command = input('Search {} has new link: {}.\n Open link Y/Default No\n'.format(each_keyword, result_link))
            if user_command.lower() == 'y':
                webbrowser.open(result_link)
        else:
            pass
    print('All result in {} is checked. Press any key to quit\n'.format(url + each_keyword))