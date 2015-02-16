#!/usr/bin/env python3

import json 

myCache = json.load(open('movieAverageCache.json', 'r'))
otherCache = json.load(open('pma459-mvAvgCache.json', 'r'))

mySum = 0
otherSum = 0
count = 0 
matchesCount = 0
for movieID in myCache.keys():
	myRating = float(myCache[movieID])
	otherRating = float(otherCache[int(movieID)])
	mySum+=myRating
	count+=1
	otherSum+=otherRating
	if(otherRating!=myRating):
		print("missmatch for " + movieID + ". myRating: " + str(myRating) + ", otherRating: " + str(otherRating))
	else:
		matchesCount+=1
		

print("matchesCount: " + str(matchesCount))
print("my average: " + str(float(mySum)/float(count)))
print("other average: " + str(float(otherSum)/float(count)))