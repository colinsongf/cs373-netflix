#!/usr/bin/env python3

import Netflix
import json

movieYearCache = json.load(open('yearlyMovieCache.json','r'))
movieRatingCache = json.load(open('pma459-mvAvgCache.json', 'r'))

resultDict = {}
yearRating = {}
for movieID in range(0,len(movieRatingCache)):
	year = 0
	try:
		year = int(movieYearCache[str(movieID)])
	except Exception:
		pass
	else:
		if str(year) in yearRating:
			l = yearRating[str(year)]
			l.append(movieRatingCache[movieID])
			yearRating[str(year)] = l
		else:
			yearRating[str(year)]=[movieRatingCache[movieID]]

for year in yearRating.keys():
	resultDict[year] = sum(yearRating[year])/len(yearRating[year])

print (json.dumps(resultDict))