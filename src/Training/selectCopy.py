#!/usr/bin/env python
# selectCopy.py - walk through a folder tree and search for file
# with certain file exteinsion. Copy these file into a new folder.

import shutil  # to copy file
import os  # to walk through folder tree

# prompt user to input folder contain file
original_folder_path = input('Enter folder contain file to copy:\n')
# prompt user to input folder to copy file
new_folder_path = input('Enter new folder contain file to copy:\n')
# prompt user to input file extension
file_ext = input('Enter file extension\n')
# walk through folder tree
for folder_name, subfolder_names, file_names in os.walk(
        os.path.join(original_folder_path)):
    # loop through list of file name in folder
    for file_name in file_names:
        # if match file extension
        if file_name.endswith(file_ext):
            # get full path of file name
            str_full_path = os.path.join(folder_name, file_name)
            # get full path of new folder to copy to
            str_new_folder_full_path = os.path.join(new_folder_path, file_name)
            # copy file to new folder and print to user
            input('copying file from: ' + str_full_path + ' to: '
                  + str_new_folder_full_path + '\n Press any key to continue..')
            shutil.copy(str_full_path, str_new_folder_full_path)
print('copy files done')
# End of code
