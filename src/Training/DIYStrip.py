#!/usr/bin/env python
# DIYStrip.py - function that takes a string and does the same thing as the strip() string method. If no other arguments are passed other than the string to strip, then whitespace characters will be removed from the beginning and end of the string. Otherwise, the characters specified in the second argument to the function will be removed from the string.

import re

#Function
def strStripString (strToStrip, strReplaceWith):
    replaceRegex = re.compile(strReplaceWith)
    return replaceRegex.sub('',strToStrip)

#UI
while(1):
	strUserString = input('type a string to strip: ')
	if strUserString == '':
		break
	strUserReplaceWith = input('type the string you want to strip: ')
	if strUserReplaceWith == '':
		strUserReplaceWith = ' '
	print (strStripString (strUserString, strUserReplaceWith))