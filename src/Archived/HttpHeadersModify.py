import requests  # fetch link content
import bs4  # search in link content
import logging  # logging error
import os  # make manage dir and file

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')
#logging.disable(logging.DEBUG)
logging.debug('Start of code')

# starting url
url = 'https://www.whatismybrowser.com/detect/what-http-headers-is-my-browser-sending'
# Modify header
headers = {
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Language':'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,ko;q=0.4,ja;q=0.3,zu;q=0.2',
    'Connection':'keep-alive',
    'Accept-Encoding':'gzip, deflate, br',
    }
page_res = requests.get(url, headers = headers)
try:
    page_res.raise_for_status()
except Exception as exc:
    input('There was a problem: {1} \nWhile checking link: {2} \nPress any key to continue'.format(exc, url))
page_res.encoding = 'utf-8'
soup = bs4.BeautifulSoup(page_res.text,'html.parser')
my_header_element = soup.find('table',{'class':'table-striped'})
my_header = my_header_element.get_text()
# Print response to a text
cur_dir = os.getcwd()
file_path = os.path.join(cur_dir,'My_Header.txt')
with open(file_path,'w') as MyHeader:
    MyHeader.write(my_header)
MyHeader.close()
print('program ended')
