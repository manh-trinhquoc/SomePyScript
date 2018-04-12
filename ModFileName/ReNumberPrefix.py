'''
Created on April 12, 2018
ReNumberPrefix.py - Numbering and add as prefix to all file and folder in folder.
@Author: manh
'''
import shutil #shutil to change file name.
import os # os to get list of all file in folder.
import logging  # logging error


logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.DEBUG)
logging.debug('Start of code')

# function to get user path. keep promping user if invalid path
def get_user_path():
    # check path exist and promt user
    while True:
        user_abs_path = input('absolute path to the folder:\n')
        if (os.path.exists(user_abs_path)):
            break
    logging.debug(user_abs_path)
    return user_abs_path
# function to get user start number. keep promping if invalid number
def get_user_start_number():
    while True:
        user_input = input('Numbering start from:\n')
        try:
            number = int(user_input)
            if number >= 0:
                break
            else:
                print('Please input a positive number\n')
        except:
            print('Please input a convertable number\n')
    number_of_character = len(user_input)
    start_number = (user_input,number,number_of_character)
    return start_number
# function to convert number to prefix
def convert_number_to_prefix(number, number_of_character):
    converted_string = str(number)
    for i in range(0,number_of_character - len(converted_string)):
        converted_string = '0'+ converted_string
    return converted_string

flag_cont_program = True #Set flag to False to end program
flag_prompt_user_input_command = True #Set flag to False so program does not prompt user command
user_input_command = '' #ok, ok A, Sk, change, End
while(flag_cont_program):
    #Prompt user to enter path to directory
    user_input_path = get_user_path()
    #Prompt user to enter start number
    user_string,start_number,number_of_character = get_user_start_number()
    next_number = start_number
    #Loop over files in the directory
    for each_file in sorted(os.listdir(user_input_path)):
        #Get full, absolute file path
        old_full_path = os.path.join (user_input_path, each_file)
        new_file_name = convert_number_to_prefix(next_number,number_of_character) + each_file
        new_full_path = os.path.join (user_input_path,new_file_name)
        #Print file rename to... Skip this step if user ok all
        if user_input_command != 'ok a':
            print('\nRenaming "%s" to "%s"...' % (each_file, new_file_name))
        #If flag_prompt_user_input_command == True ->Prompt user to enter command.
        while (flag_prompt_user_input_command):
            user_input_command = input ('Enter command (ok), skip (sk) ok all (ok a)' +
                ', change path or prefix (change), end program (end)\n')
            if user_input_command in ['ok', 'sk', 'ok a','change', 'end']:
                break
        #Input ok -> Rename file
        if user_input_command == 'ok':
            shutil.move (old_full_path, new_full_path)
            next_number = next_number + 1
            print ('File name has been changed')
        #Input sk -> Skip this file
        elif user_input_command == 'sk':
            print ('Changing name for this file has been skipped')
            continue
        #Input ok a -> Rename all files then end program.
        elif user_input_command == 'ok a':
            shutil.move (old_full_path, new_full_path)
            next_number = next_number + 1
            flag_prompt_user_input_command = False
        #Input change -> Return step: Prompt user to enter path to directory
        elif user_input_command == 'change':
            break
        #Input end -> End program
        elif user_input_command == 'end':
            flag_cont_program = False
            print ('Program will be end. File name will not changed')
            break
    #End program after loop all file
    else:
        flag_cont_program = False
print('program ended')
#End Code
