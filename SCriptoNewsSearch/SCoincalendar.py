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
import re  # search keyword in content
import time  # sleep

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.DEBUG)
logging.debug('Start of code')

cur_dir = os.getcwd()
file_path = os.path.join(cur_dir,'DB','SNewsSearch')
vietNewsShelf = shelve.open(file_path)
list_keywords = []
for value in vietNewsShelf.values():
    list_keywords.append(''.join(value).lower())
url = 'http://www.coincalendar.info'              # starting url
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
for each_keyword in list_keywords:
    # Download the page.
    print('Checking coincalendar key word: {}...'.format(each_keyword))
    time.sleep(5)
    page_res = requests.get(url)
    try:
        page_res.raise_for_status()
    except Exception as exc:
        input('There was a problem: {1} \nWhile checking link: {2} \nPress any key to quit'.format(exc, url))
        sys.exit()
    page_res.encoding = 'utf-8'
    soup = bs4.BeautifulSoup(page_res.text,'html.parser')
    # The html of all search results.
    list_element_all_result = soup.select('div[class="eventon_list_event event"]')
    # The links of current result
    for each_element in list_element_all_result:
        soup = bs4.BeautifulSoup(str(each_element),'html.parser')
        list_element_link_tag = soup.select('div[class="evo_event_schema"] a')
        result_link = list_element_link_tag[0].get('href')
        # get content
        list_element_content_tag = soup.select('div[class="evo_event_schema"] span')
        content = list_element_content_tag[0].getText()
        # regex search in content
        re_search = re.search(each_keyword.lower(),content.lower())
        # if found regex
        logging.debug('search: {} in {}'.format(each_keyword, content))
        logging.debug('re_search type: {}'.format(str(type(re_search))))
        if re_search is not None:
            # Check link in database
            if result_link not in old_links:
                file_path = os.path.join(cur_dir,'DB','OldLink.txt')
                with open(file_path,'a+') as txt_OldLink:
                    txt_OldLink.write(result_link + '\n')
                txt_OldLink.close()
                user_command = input('Search {} has new link: {}.\n Open link Y/Default No\n'.format(each_keyword, result_link))
                if user_command.lower() == 'y':
                    webbrowser.open(result_link)
    print('All result of keyword {} in {} is checked.\n'.format(each_keyword, url))
print('All keywords are checked. Program end\n')
