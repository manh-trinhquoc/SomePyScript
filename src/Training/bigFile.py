#!/usr/bin/env python
# bigFile.py - walk through a folder tree and search for large file

import os  # To wakl through tree and get file size
import re  # regex to check user input is numer

# promt user to enter folder path
folder_path = input('Enter folder path:\n')
# prompt user to enter file size and change to int
while True:
    file_size_regex = re.search('^\d+$', input('Enter file size in MB\n'))
    # print(file_size_regex) # comment out when finish
    if file_size_regex:
        user_file_size = int(file_size_regex.group())
        # print(file_size) # comment out when finish
        break

# walk through to folder tree and get file size
for folder_name, sub_folders, file_names in os.walk(folder_path):
    for file_name in file_names:
        file_size = os.path.getsize(os.path.join(folder_name, file_name))
        file_size = int(file_size/1024/1024)
        # print file path and file size if large file
        if file_size >= user_file_size:
            print(file_name + ' is a large file: ' + str(file_size) + 'MB')
