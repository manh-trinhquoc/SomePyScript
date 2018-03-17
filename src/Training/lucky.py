'''
Created on Nov 18, 2017
lucky.py - search key word from Window + R command. Open first 5 links in browser.
@author: manh.trinhquoc
'''
import sys  # read Window + R command
import requests  # fetch result page
import bs4  # analyze fetched page
import webbrowser  # open link in browser
import time  # sleep
import logging  # logging error
logging.basicConfig(filename='programLog.txt', level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')
#logging.disable(logging.DEBUG)
logging.debug('Start of code')


# TODO: create fake input to test
sys.argv[0] = 'lucky'
sys.argv.append('29 Awesome Things You Didnt Know About Google')
# End of fake input. Comment all out when finish

print('Googling...') # display text while downloading the Google page
res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
try:
    res.raise_for_status()
except Exception as exc:
    input('There was a problem: {}.\nPress any key to quit program.'.format(exc))
    sys.exit()
# Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text)
logging.debug('\n' + res.text + '\n')
# Open a browser tab for each result.
linkElems = soup.select('h3 a')
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    webbrowser.open('http://google.com' + linkElems[i].get('href'))
    logging.debug(linkElems[i])
    time.sleep(2)
