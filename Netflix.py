#!/usr/bin/env python3

import json 
import fileinput
import math
import string

movieRatingCache = json.load(open('pma459-mvAvgCache.json', 'r'))
answersCache = json.load(open('pma459-answersCache.json', 'r'))

def getPredictedRating(userID,movieID):
	return float(movieRatingCache[int(movieID)])

def getRealRating(userID,movieID):
	return float(answersCache[movieID][userID])

def getRMSE(sqrtSum,numElements):
	return round(((sqrtSum)/numElements)**0.5,2)

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
		predictedRating = getPredictedRating(userID,movieID)
		print(round(predictedRating,2))
		realRating = getRealRating(userID,movieID)
		diff = predictedRating - realRating
		sqrtSum += diff **2
		count+=1

print ("RMSE: " + str(getRMSE(sqrtSum,count)))




