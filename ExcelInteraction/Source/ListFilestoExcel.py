'''
created in April 1st,2018
user input link to a folder. script will list all files in folder to an excel and make link to file.
Author: manh
'''

import os  # open file path
import logging  # logging error


logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.DEBUG)
logging.debug('Start of code')

# function to get user path. keep promp user if invalid path
def get_user_path():
    # check path exist and promt user
    while True:
        user_abs_path = input('absolute path to the folder:\n')
        if (os.path.exists(user_abs_path)):
            break
    logging.debug(user_abs_path)
    return user_abs_path

# prompt user to input path
user_folder_path = get_user_path()
# TODO: open new excel file

# TODO: lists file to excel with link

# TODO: save excel to same folder

print('program finished')