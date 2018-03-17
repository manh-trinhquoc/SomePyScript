#!/usr/bin/env python
# MadLibs.py - Replace ADJECTIVE, NOUN, ADVERB, VERB in text.

import re

adjective_regex = re.compile (r'ADJECTIVE')
noun_regex = re.compile (r'NOUN')
adverb_regex = re.compile (r'ADVERB')
verb_regex = re.compile (r'VERB')

#Prompt user to enter text
text_orginal = input('Enter text with ADJECTIVE, NOUN, ADVERB and VERB:\n')
#Prompt user to enter text to replace ADJECTIVE, NOUN, ADVERB, VERB if there were in text.
adjective_replace = input('Enter word to replace ADJECTIVE:')
noun_replace = input ('Enter word to replace NOUN:')
adverb_replace = input ('Enter word to replace ADVERB:')
verb_replace = input ('Enter word to replace VERB:')
#Creat new text and print.
text_return = adjective_regex.sub(adjective_replace,text_orginal)
text_return = noun_regex.sub (noun_replace, text_return)
text_return = adverb_regex.sub (adverb_replace, text_return)
text_return = verb_regex.sub (verb_replace, text_return)
print (text_return)
#TODO: save new text to text file
text_file = open('.\\'+ noun_replace + '.txt','w')
text_file.write(text_return)
text_file.close()
