#!/usr/bin/env python3

import json

movieRatingCache = json.load(open('pma459-mvAvgCache.json', 'r'))
answersCache = json.load(open('pma459-answersCache.json', 'r'))
userAverageRatingCache = json.load(open('pma459-usrAvgCache.json', 'r'))
movieYearCache = json.load(open('yearlyMovieCache.json','r'))
yearAverageCache = json.load(open('yearAverageCache.json','r'))

resultDict = {}
numMisses = [0]
numEntries = [0]

for movieID in answersCache.keys():
	for user in answersCache[movieID]:
		try:
			int(movieYearCache[movieID])
		except Exception:
			numMisses[0]+=1
		else:
			year = movieYearCache[movieID]
			rating = answersCache[movieID][user]
			numEntries[0]+=1
			if user in resultDict:
				resultDict[user].append(rating)
			else:
				resultDict[user] = [rating]


print("misses: " + str(numMisses[0]))
print("numEntries: " + str(numEntries[0]))
print(resultDict)