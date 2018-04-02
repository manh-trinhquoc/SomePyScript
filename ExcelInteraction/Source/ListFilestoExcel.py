'''
created in April 1st,2018
user input link to a folder. script will list all files in folder to an excel and make link to file.
Author: manh
'''

import os  # open file path
import logging  # logging error
import openpyxl  # excel package
from openpyxl import Workbook
import re  # regex to check file name

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
# Open new excel file
excel_wb = Workbook()
# Get active sheet
excel_ws = excel_wb.active
# lists file to excel with link
#Loop over files in the directory
row_count = 0
for each_file in os.listdir(user_folder_path):
    # Skip hidden, temporary file
    is_temp = re.search('^~', each_file)
    if (is_temp != None):
        logging.debug('{0} is a temp file\n'.format(each_file))
        continue
    # Skip this own xlsx file
    if (each_file == '001FileNameList.xlsx'):
        continue
    # Get full, absolut file path
    file_full_path = os.path.join (user_folder_path, each_file)
    row_count = row_count + 1
    excel_ws['A{}'.format(str(row_count))] = '{}'.format(str(row_count))
    excel_ws['B{}'.format(str(row_count))] = each_file
    # Add hyperlink to file
    excel_ws['C{}'.format(str(row_count))] = '=HYPERLINK("{}")'.format(each_file)
# Save excel to same folder
file_full_path = os.path.join (user_folder_path, '001FileNameList.xlsx')
# prompt user if file exits
while (True):
    if (os.path.exists(file_full_path)):
        input('file existed. Please delete old file before saving')
    else:
        excel_wb.save(file_full_path)
        break
print('program finished')
