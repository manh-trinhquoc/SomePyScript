'''
Created on Nov 23, 2017
Srcapt Coinmarket for price-push notification when price exceed a value
@author: General
'''

import sys  # quit program when error
import logging  # logging error


logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.DEBUG)
logging.debug('Start of code')

command = input('{} price: {}'.format(sys.argv[1], sys.argv[2]))
#input('{} price: {}'.format(each_coin, price))

