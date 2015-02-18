#!/usr/bin/env python3

import random
import json


answersCache = json.load(open('pma459-answersCache.json', 'r'))
linesWritten = 0
while(linesWritten<=100):
	movieID = random.randint(1,17770)
	while(str(movieID) not in answersCache):
		movieID = random.randint(1,17770)
	print(str(movieID) + ":")
	validUsers = list(answersCache[str(movieID)].keys())
	numRatings = min(random.randint(1,len(validUsers)),20)
	ratingsGiven = 0
	while(ratingsGiven<numRatings):
		userID = validUsers[ratingsGiven]
		ratingsGiven+=1
		print(userID)
		linesWritten+=1
		

print("linesWritten: " + str(linesWritten))

