#!/usr/bin/env python
tableData1 = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(tableData):
	colWidth = [0]*len(tableData)
	for line in range(len(tableData)):
		for col in range(len(tableData[line])):
			if colWidth[line]<len(tableData[line][col]):
				colWidth[line] = len(tableData[line][col])
	for line in range(len(tableData)):
		for col in range(len(tableData[line])):
			print(tableData[line][col].rjust(max(colWidth)+1),end="")
		print('\n')

printTable(tableData1)