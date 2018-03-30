#!/usr/bin/env python
# APrefix.py - Add prefix to all file in folder.

import shutil #shutil to change file name.
import os # os to get list of all file in folder.
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

flag_cont_program = True #Set flag to False to end program
flag_prompt_user_input_command = True #Set flag to False so program does not prompt user command
user_input_command = '' #ok, ok A, Sk, change, End
while(flag_cont_program):
    #Prompt user to enter path to directory
    user_input_path = get_user_path()
    #Prompt user to enter prefix
    user_input_prefix = input ('Enter Prefix to add:\n')
    #Loop over files in the directory
    for each_file in os.listdir(user_input_path):
    	#Get full, absolut file path
        old_full_path = os.path.join (user_input_path, each_file)
        new_full_path = os.path.join (user_input_path, user_input_prefix + each_file)
        #Print file rename to... Skip this step if user ok all
        if user_input_command != 'ok a':
            print('\nRenaming "%s" to "%s"...' % (old_full_path, new_full_path))
        #If flag_prompt_user_input_command == True ->Prompt user to enter command.
        while (flag_prompt_user_input_command):
            user_input_command = input ('Enter command (ok), skip (sk) ok all (ok a)' +
        	    ', change path or prefix (change), end program (end)\n')
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