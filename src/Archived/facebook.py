'''
Created on Nov 13, 2017
vietNews.py - open list of Vietnamese news pages when bored.
Open in Windows + R
Command
<Empty> - Open links in browser
Add [Address Link] - Add address to database
List - List all links saved in database
Del [No. of Address Link] - Delete link in database
@author: General
'''
import shelve  # save variable to database
import sys  # get parameter in Window + R command
import pyperclip  # get link in clip board
import webbrowser  # manage web browser
import os  # get directory to database
import time  # make script sleep for seconds
import logging  # logging error
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.DEBUG)
logging.debug('Start of code')


# TODO: create fake input to test
#sys.argv[0] = 'vietNews.py'
#sys.argv.append('Del')
#sys.argv.append('1')
# End of fake input. Comment all out when finish
vietNewsShelf = shelve.open(os.path.join('C:\\001MyPythonScript\\src','facebook'))
number_of_address = len(vietNewsShelf)
logging.debug('len(vietNewsShelf) = {}'.format(len(vietNewsShelf)))
invalid_user_input = False
list_shelf_temp = []  # list for re-arrange shelf
# get user command
# command line Add address link
logging.debug('command: {}'.format(sys.argv))
if len(sys.argv) == 1:
    logging.debug('len of sys.argv = 1')
    # Go to address in shelve database
    for each in list(vietNewsShelf.keys()):
            webbrowser.open(vietNewsShelf[each])
            time.sleep(2) 
elif len(sys.argv) == 2:
    logging.debug('len of sys.argv = 2')
    if sys.argv[1].lower() == 'add':
        logging.debug('sys.argv[1] = add')
        # Get address from clipboard.
        address = pyperclip.paste()
        # save address to database shelve
        no_of_address = number_of_address + 1
        vietNewsShelf[str(no_of_address)] = address
    # command line List
    elif sys.argv[1].lower() == 'list':
        logging.debug('sys.argv[1] = list')
        # List all address in database shevle
        logging.debug('vietNewsShelf.key() = '.format(vietNewsShelf.keys()))
        list_key = list(vietNewsShelf.keys())
        logging.debug('list_key = {}'.format(list_key))
        for each in list_key:
            print(each + ' ' + vietNewsShelf[each])
            logging.debug('key = {}, address = {}'.format(each, vietNewsShelf[each]))
        input('')
    # command line Del
    elif sys.argv[1].lower() == 'del':
        # Delete all shelve database
        decide = input('Are you sure you want to del all link?\n Y:Yes/Default: No\n')
        if decide.lower() == 'y':
            for each in list(vietNewsShelf.keys()):
                del vietNewsShelf[each]
            input('You have del all link')
        else:
            input('You did not input Y. Not any file has been del')
    else:
        invalid_user_input = True
elif len(sys.argv) == 3:
    # command add
    if sys.argv[1].lower() == 'add':
        address = sys.argv[2]
        # save address to database shelve
        no_of_address = number_of_address + 1
        vietNewsShelf[str(no_of_address)] = address
    # command del
    elif sys.argv[1].lower() == 'del':
        no_of_address = int(sys.argv[2])
        # TODO: handle error fail to convert to int
        # TODO: handle error if no key
        # del address at No.
        decide = input('Are you sure you want to del {} {}\n Y: Yes/Default: No\n'.format(no_of_address,vietNewsShelf[str(no_of_address)]))
        if decide.lower() == 'y':
            del vietNewsShelf[str(no_of_address)]
            input('Link have been del')
            # TODO: Re-arrange database and print new database to user
            for each1 in list(vietNewsShelf.keys()):
                list_shelf_temp.append(vietNewsShelf[each1])
            for each2 in list(vietNewsShelf.keys()):
                del vietNewsShelf[each2]
            for each3 in range(len(list_shelf_temp)):
                vietNewsShelf[str(each3+1)] = list_shelf_temp[each3]
        else:
            input('You did not input Y. File have not been del')
    else:
        invalid_user_input = True
else:
    invalid_user_input = True
if invalid_user_input == True:
    input('''Command
    <Empty> - Open links in browser
    Add [Address Link] - Add address to database
    List - List all links saved in database
    Del [No. of Address Link] - Delete link in database    
    ''')
vietNewsShelf.close()
