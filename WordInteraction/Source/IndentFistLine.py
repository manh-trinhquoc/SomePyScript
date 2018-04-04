'''
Created on April 04, 2018
User input name of Style, number of indentation (inch),
absolute path to folder.
Script change fist line indentation of all docx file in folder, not include subfolder.
Author:Manh
'''

import docx  # docx module
from docx.shared import Inches
import os  # open file path
import logging  # logging error

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.DEBUG)
logging.debug('Start of code')

# function to check file extension. do not include "."
def is_extension(file_name, file_extension):
    return file_name.endswith(file_extension)
    
# function to get user path. keep promp user if invalid path
def get_user_path():
    # check path exist and promt user
    while True:
        user_abs_path = input('absolute path to the folder:\n')
        if (os.path.exists(user_abs_path)):
            break
    logging.debug(user_abs_path)
    return user_abs_path

# Prompt user to input file path
user_path = get_user_path()
# Prompt user to input style name 1, inches to indent 1,...
user_string = input('list of style and inches to identation: style 1,\
 identation, style 2, identation 2..\n')
# Save style to dictionary
list_string = user_string.split(',')  # get each parameter
# Remove space character
for i in range(0,len(list_string)):
    list_string[i] = list_string[i].strip() 
dic_user_style ={}
for count in range(len(list_string)):
    if (count % 2 == 0):
        try:
            dic_user_style.update({list_string[count]:float(list_string[count + 1])})
        except:
            dic_user_style.update({list_string[count]:0})
# Iteration over files in folder
for each_file in os.listdir(user_path):
    # Check file type
    if ( not is_extension(each_file, '.docx')):
        logging.debug('{0} is not a .docx file\n'.format(file_full_path))
        continue
    #Get full, absolut file path
    file_full_path = os.path.join (user_path, each_file)
    # Open word file
    try:
        file_docx = docx.Document(file_full_path) 
        logging.debug('open file: '+file_full_path +'\n')
    except:
        logging.warning('can not open file: '+file_full_path +'\n')
        continue
    # Loop through style dictionary
    for user_style in dic_user_style.keys():
        logging.debug('check style: '+user_style +'\n')
        # Indentation
        if (user_style in file_docx.styles):
            file_docx.styles[user_style].paragraph_format.first_line_indent \
            = Inches(dic_user_style[user_style])
    # Save file
    file_docx.save(file_full_path)
    logging.debug('save docx file:{0}'.format(file_full_path))
# Print program finish
print('Program finished')
