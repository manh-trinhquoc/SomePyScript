'''
Replace character in file name.
'''
import shutil # shutil to change file name. 
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
# function to get user string to replace
def get_string_to_replace():
    user_string = input ('String to replace\n')
    return user_string
# function to get user string to replace with
def get_string_replace_with():
    user_string = input ('String to replace with\n')
    return user_string
# function to check if file is temporary
def is_temp(file_name):
    if (file_name.startswith('~')):
        return True
    else:
        return False
#function get new file name
def get_new_file_name(old_file_name,old_string,new_string):
    new_file_name = old_file_name.replace(old_string,new_string)
    return new_file_name

# Promp user for folder path
user_input_path = get_user_path()
# Promp user for string to replace
user_string_to_replace = get_string_to_replace()
# Promp user for string to replace with
user_string_replace_with = get_string_replace_with()
# program behave depend on user input command
user_input_command = '' #ok, ok A, Sk, change, End
flag_prompt_user_input_command = True #Set flag to False so program does not prompt user command
# Loop through all file
for each_file in os.listdir(user_input_path):
    # Skip temporary file
    if (is_temp(each_file)):
        logging.debug('{0} is a temp file\n'.format(each_file))
        continue
    # Get new file name
    new_file_name = get_new_file_name(each_file, user_string_to_replace,
                                          user_string_replace_with)
    # Get old full, absolut file path
    old_full_path = os.path.join (user_input_path, each_file)
    # Get new full, absolut file path
    new_full_path = os.path.join (user_input_path, new_file_name)
    # Promp user for change file option
    # Print file rename to... Skip this step if user ok all
    if user_input_command != 'ok a':
        print('\nRenaming "%s" to "%s"' % (each_file, new_file_name))
     #If flag_prompt_user_input_command == True ->Prompt user to enter command.
    while (flag_prompt_user_input_command):
        user_input_command = input ('Enter command (ok), skip (sk), ok all\
(ok a), end program (end)\n')
        if user_input_command in ['ok', 'sk', 'ok a', 'end']:
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
    #Input end -> End program
    elif user_input_command == 'end':
        input ('Program will be end. File name will not changed. Hit any key to continue')
        break
# Print finish program
print('program finished')
