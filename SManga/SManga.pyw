'''
Created on Nov 13, 2017
SManga.pyw - Get command and transfer to corresponding .bat
@author: General
'''
import shelve  # save variable to database
import sys  # get parameter in Window + R command
import pyperclip  # get link in clip board
import os  # get directory to database
import logging  # logging error
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')
#logging.disable(logging.DEBUG)
logging.debug('Start of code')


# TODO: create fake input to test
# sys.argv[0] = 'SManga.pyw'
# sys.argv.append('List')
# sys.argv.append('HunterX')
# End of fake input. Comment all out when finish

if len(sys.argv) == 1:
    logging.debug('len of sys.argv = 1')
    os.system('SMangaFetch')
else:
    logging.debug('len of sys.argv > 1')
    command = ' '.join(sys.argv[1:])
    command = 'SMangaUI {}'.format(command)
    logging.debug(command)
    #os.chdir('C:\\')
    #logging.debug(os.getcwd())
    #os.system('python SMangaUI.py list')
    os.system(command)
