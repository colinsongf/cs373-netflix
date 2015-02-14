#!/usr/bin/env python3

import fileinput
import json
import string

file = open("dates.txt",'r')
resultDict = {}
for line in file:
	elements = line.split(",")
	movieID = elements[0]
	year = elements[1]
	resultDict[movieID] = year


print(json.dumps(resultDict))

