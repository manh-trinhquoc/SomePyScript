'''
Created on Nov 13, 2017
mapIT.py - open google map in the browser using the address from the command
line or clip board
@author: manh.trinhquoc
'''
import webbrowser  # launching the web browser
import sys  # reading command line argument
import pyperclip  # get data from clip board
if len(sys.argv) > 1:
    # Get address from command line.
    address = ' '.join(sys.argv[1:])
else:
    # Get address from clipboard.
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)
