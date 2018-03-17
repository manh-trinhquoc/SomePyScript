#!/usr/bin/env python
# RegexSearch.py - Open text file and print line match the regex pattern. Regex entered by user.

import re, os

#Prompt user to enter regex pattern
regex_user = input ('Enter Regex Pattern:\n')
regex_pattern = re.compile (regex_user)
#TEMP:print (regex_pattern.search ('My number is 415-555-4242'))
#Iterate all text file in folder
for file_name in os.listdir('.\\'):
	if (re.search('.txt$',file_name) != None):
		#Open all text file
		text_file = open ('.\\' + file_name,'r')
		#Find regex pattern and print
		regex_match = regex_pattern.search (text_file.read())
		#TEMP:regex_match = regex_pattern.search ('My number is 415-555-4242')
		if (regex_match != None):
			print (regex_match.group() + ' in file: ' + file_name)
		else:
			print ('Not any match in file: ' + file_name)
		#TEMP: print (text_file)
		#Close text file
		text_file.close()
#Prompt finish program
#TEMP:print ('RegexSearch.py finished')