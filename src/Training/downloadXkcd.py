'''
Created on Nov 18, 2017
downloadXkcd.py - Downloads every single XKCD comic.
@author: General
'''
import requests  # fetch link content
import bs4  # search in link content
import os  # make manage dir and file
import sys  # quit program when error
import time  # make script sleep for seconds
import logging  # logging error


logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.DEBUG)
logging.debug('Start of code')
url = 'http://xkcd.com//1900'              # starting url
os.makedirs('xkcd', exist_ok=True)   # store comics in ./xkcd
while True:
    # Download the page.
    print('Downloading page %s...' % url)
    time.sleep(1)
    res = requests.get(url)
    try:
        res.raise_for_status()
    except Exception as exc:
        input('There was a problem: {}\nPress any key to quit'.format(exc))
        sys.exit()
    soup = bs4.BeautifulSoup(res.text)
    # Find the URL of the comic image.
    comicElem = soup.select('#comic img')
    if comicElem == []:
        print('Could not find comic image.')
    else:
        try:
            comicUrl = 'http:' + comicElem[0].get('src')
            # get alter link if had
            if comicElem[0].get('srcset') is not None:
                comicUrl = 'http:' + comicElem[0].get('srcset').split(' ')[0]
            # Download the image.
            print('Downloading image %s...' % (comicUrl))
            res = requests.get(comicUrl)
            res.raise_for_status()
        except requests.exceptions.MissingSchema:
            # skip this comic
            prevLink = soup.select('a[rel="prev"]')[0]
            url = 'http://xkcd.com' + prevLink.get('href')
            continue
        # Save the image to ./xkcd.
        # TODO: check duplicate image name
        image_full_path = os.path.join('xkcd', os.path.basename(comicUrl))
        if os.path.exists(image_full_path):
            input('reach last link: {}'.format(comicUrl))
            sys.exit()  # image already saved
        else:
            imageFile = open(image_full_path, 'wb')
            for chunk in res.iter_content(100000):
                imageFile.write(chunk)
            imageFile.close()
    # Get the Prev button's url.
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com' + prevLink.get('href')
print('Done.')
