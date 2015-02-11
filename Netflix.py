#!/usr/bin/env python3

import json 
import fileinput
import math
import string

movieRatingCache = json.load(open('pma459-mvAvgCache.json', 'r'))
answersCache = json.load(open('pma459-answersCache.json', 'r'))


#read in a line
movieID = ""
sqrtSum = 0
count = 0
for line in fileinput.input():
	if ":" in line:
		#we have a new movie
		movieID = line.split(":")[0]
		print(movieID + ":")
	else:
		#we are predicting the rating userID gave to movieID
		userID = line.rstrip()
		predictedRating = float(movieRatingCache[int(movieID)])
		print(round(predictedRating,2))
		realRating = float(answersCache[movieID][userID])
		diff = predictedRating - realRating
		sqrtSum += diff **2
		count+=1
sqrtError = round(((sqrtSum)/count)**0.5,2)
print ("RMSE: " + str(sqrtError))



