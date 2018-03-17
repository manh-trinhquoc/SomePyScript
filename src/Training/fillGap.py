#!/usr/bin/env python
# fillGap.py - walk through a folder tree, find all files with given prefix,
# locate gap in numbering, rename all the later file to close the gap

# import os to walk throug folder tree
import os
# import regex to find file with given prefix
import re
# import shutil to rename file
import shutil

# list of original file name
lst_org_file_names = []
# list file name without gap
lst_no_gap_file_names = ''


# define function get file number. parameter: filename;
# prefix, return file number
def get_file_number(file_name, prefix):
    file_number = file_name[len(prefix):]
    return int(file_number)


# prompt user to enter prefix
str_user_prefix = input('Enter prefix:\n')
# create prefix regex object
prefix_obj_regex = re.compile(r'^' + str_user_prefix + r'\d+$')
# create extension regex object
ext_obj_regex = re.compile(r'\.\w{2,4}$')
# prompt user to enter folder path
str_user_folder = input('Enter folder path:\n')
# walk through folder
for folder_path, subfolder_names, file_names in os.walk(str_user_folder):
    for file_name in file_names:
        # find file name extension
        obj_ext_re = ext_obj_regex.search(file_name)
        if obj_ext_re is None:
            str_file_name_only = file_name
        else:
            # get file name lenght
            _len = len(file_name) - len(obj_ext_re.group())
            # split file name and extension
            str_file_name_only = file_name[0:_len]
            # print (str_file_name_only)  # comment out when finish
        # check if file has legit prefix
        obj_prefix_re = prefix_obj_regex.search(str_file_name_only)
        if obj_prefix_re is None:
            print('There is none file match your prefix in this folder_path: '
                  + folder_path)
            break
        else:
            # add file name only to list of file with prefix
            lst_org_file_names.append(str_file_name_only)
            # get file number of current name
            current_number = get_file_number(
                str_file_name_only, str_user_prefix)
            # print('current_number: ' + str(current_number))  # comment out
            # get file number of first position
            fist_number = get_file_number(
                lst_org_file_names[0], str_user_prefix)
            # locate gap
            gap_number = (current_number - fist_number
                          - len(lst_org_file_names) + 1
                          )
            if gap_number < -1:
                print('this case should not happend. re-check logic')
            elif gap_number == -1:
                # get new file name
                str_new_number = str(current_number + 1)
                str_new_file_name = (
                    str_user_prefix
                    + '0'*(len(str_file_name_only)  # get number of '0'
                           - len(str_user_prefix)
                           - len(str_new_number)
                           )
                    + str_new_number
                    + obj_ext_re.group()  # add file extension
                    )
                # change file name
                shutil.move(
                    os.path.join(folder_path, file_name),
                    os.path.join(folder_path, str_new_file_name)
                    )
            elif gap_number == 0:
                pass
            else:
                # get new file name
                str_new_number = str(fist_number + len(lst_org_file_names) - 1)
                str_new_file_name = (
                    str_user_prefix
                    + '0'*(len(str_file_name_only)  # get number of '0'
                           - len(str_user_prefix)
                           - len(str_new_number)
                           )
                    + str_new_number
                    + obj_ext_re.group()  # add file extension
                    )
                # print(str_new_file_name)  # comment out when finish
                # change file name
                # print('new file name:\n' + os.path.join(
                # folder_path,str_new_file_name))
                shutil.move(
                    os.path.join(folder_path, file_name),
                    os.path.join(folder_path, str_new_file_name)
                    )
print('Filling Gap done')
