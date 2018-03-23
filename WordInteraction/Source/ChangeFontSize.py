'''
Created on March 23, 2018
User input name of Style, font_size, absolute path to folder.
Script change font size of all docx file in folder, not include subfolder.
Author:Manh
'''

import docx  # docx module
from docx.shared import Pt  # font module
import os  # open file path
import logging  # logging error


logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.DEBUG)
logging.debug('Start of code')

# User input style 1, size 1, style 2, size 2...
user_string = input('list of style and size: style 1, size, style 2, size 2..\n')

# Save to dictionary
list_string = user_string.split(',')
dic_user_style ={}
for count in range(len(list_string)):
    if (count % 2 == 0):
        try:
            dic_user_style.update({list_string[count]:int(list_string[count + 1])})
        except:
            pass
# User input absolute path
# check path exist and promt user
while True:
    user_abs_path = input('absolute path to the folder:\n')
    if (os.path.exists(user_abs_path)):
        break
logging.debug(user_abs_path)
# open word file
#Loop over files in the directory
for each_file in os.listdir(user_abs_path):
    #Get full, absolut file path
    file_full_path = os.path.join (user_abs_path, each_file)
    # TODO: only get docx file
    file_path_splited = file_full_path.split('.')
    extend_part = file_path_splited[len(file_path_splited)-1]
    file_name = file_path_splited[len(file_path_splited)-2].split('/')
    file_name = file_name[len(file_name)-1]
    if ( extend_part != 'docx'):
        logging.debug('{0} is not a .docx file\n'.format(file_full_path))
        continue
    file_docx = docx.Document(file_full_path) 
    logging.debug('open file: '+file_full_path +'\n')
    # Loop through style dictionary
    for user_style in dic_user_style.keys():
        logging.debug('check style: '+user_style +'\n')
        if (user_style in file_docx.styles):
            file_docx.styles[user_style].font.size = Pt(dic_user_style[user_style])
    # Save as ...-new.docx
    file_full_path_new = os.path.join(user_abs_path,file_name + '_new.docx')
    file_docx.save(file_full_path_new)
    logging.debug('save new docx file:{0}'.format(file_full_path_new))
