#!/usr/bin/env python
# ASuffix.py - Add suffix to all file in folder.

import shutil, os #shutil to change file name. os to get list of all file in folder.
import re #Regex to find .ext
flag_cont_program = True #Set flag to False to end program
flag_prompt_user_input_command = True #Set flag to False so program does not prompt user command
user_input_command = '' #ok, ok A, Sk, change, End

#Define function to get new_full_path of file. Input file_path, file_name, suffix
def get_new_full_path(file_path, file_name, suffix):
    #Use regex to find filename.ext.
    ext_path = re.search(r'(\.\w*)$',file_name)
    if ext_path == None:
    	#Join file path, filename + suffix
    	return os.path.join (file_path, file_name + suffix)
    else:
        #Split filename and .ext.
        file_name_split = file_name.split('.')
        #Join filename + suffix + .ext
        file_name = file_name_split[0]
        for each in range(1,len(file_name_split)-1):
        	file_name = file_name +'.' + file_name_split[each]
        file_name = file_name + suffix + '.' + file_name_split[len(file_name_split)-1]
        return os.path.join (file_path, file_name)

while(flag_cont_program):
    #Prompt user to enter path to directory
    user_input_path = input('Enter path to directory:\n')
    #Prompt user to enter suffix
    user_input_suffix = input ('Enter suffix to add:\n')
    #Loop over files in the directory
    for each_file in os.listdir(user_input_path):
    	#Get full, absolut file path
        old_full_path = os.path.join (user_input_path, each_file)
        new_full_path = get_new_full_path (user_input_path, each_file, user_input_suffix)
        #Print file rename to... Skip this step if user ok all
        if user_input_command != 'ok a':
            print('\nRenaming "%s" to "%s"...' % (old_full_path, new_full_path)) 
        #If flag_prompt_user_input_command == True ->Prompt user to enter command.
        while (flag_prompt_user_input_command):
            user_input_command = input ('Enter command (ok), skip (sk) ok all (ok a)' +
        	    ', change path or suffix (change), end program (end)\n')
            if user_input_command in ['ok', 'sk', 'ok a','change', 'end']:
            	break
        #Input ok -> Rename file
        if user_input_command == 'ok':
            shutil.move (old_full_path, new_full_path)
            input ('File name has been changed. Hit any key to continue')
        #Input sk -> Skip this file
        elif user_input_command == 'sk':
            input ('Changing name for this file has been skipped. Hit any key to continue')
            continue
        #Input ok a -> Rename all files then end program.
        elif user_input_command == 'ok a':
            shutil.move (old_full_path, new_full_path)
            flag_prompt_user_input_command = False
        #Input change -> Return step: Prompt user to enter path to directory
        elif user_input_command == 'change':
            break
        #Input end -> End program
        elif user_input_command == 'end':
    	    flag_cont_program = False
    	    input ('Program will be end. File name will not changed. Hit any key to continue')
    	    break
    #End program after loop all file
    else:
    	flag_cont_program = False
#End Code