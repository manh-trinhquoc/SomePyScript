#!/usr/bin/env python
# isStrongPassword.py - check if password has all following condition: >8 character, contain both upper case and lower case, at least 1 digit.

import re

#TODO: define isStrongPassword
def isStrongPassword(password):
	haveUpper = re.compile(r'[A-Z]')
	haveLower = re.compile(r'[a-z]')
	haveDigit = re.compile(r'[0-9]')
	if len(password) < 8:
		return False
	if haveUpper.search(password) == None:
		return False
	if haveLower.search(password) == None:
		return False
	if haveDigit.search(password) == None:
		return False
	return True

#TODO: create UI
while(1):
	userPassword = input('type password: ')
	if userPassword == '':
		break
	else:
		print('Your password is strong: '+ str(isStrongPassword(userPassword)))
		input('press any key to continue')