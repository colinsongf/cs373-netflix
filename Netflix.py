#!/usr/bin/env python3
import sys 
import json 
import fileinput
import math
import string

CUSTOMER_ID_LIMIT = 2649429
MOVIE_ID_LIMIT = 17770

movieRatingCache = json.load(open('pma459-mvAvgCache.json', 'r'))
answersCache = json.load(open('pma459-answersCache.json', 'r'))

def getPredictedRating(userID,movieID):
	userID = int(userID)
	movieID = int(movieID)

	assert movieID >= 1 and movieID <= MOVIE_ID_LIMIT 
	return float(movieRatingCache[int(movieID)])
	

def getRealRating(userID,movieID):
	userID = int(userID)
	movieID = int(movieID)

	assert movieID >=1  and movieID <= MOVIE_ID_LIMIT
	assert userID >= 1 and userID <= CUSTOMER_ID_LIMIT 	
	try:
		return float(answersCache[str(movieID)][str(userID)])
	except KeyError:
		return 0
	

def getRMSE(sqrtSum,numElements):
	return round(((sqrtSum)/numElements)**0.5,2)

def netflixRatingPredictor():
	#read in a line
	movieID = ""
	sqrtSum = 0
	count = 0
	for line in fileinput.input():
		if ":" in line:
			#we have a new movie
			movieID = line.split(":")[0]
			#print(movieID + ":")
		else:
			#we are predicting the rating userID gave to movieID
			userID = line.rstrip()
			predictedRating = getPredictedRating(int(userID),int (movieID))
			#print(round(predictedRating,2))
			realRating = getRealRating(userID,movieID)
			diff = predictedRating - realRating
			sqrtSum += diff **2
			count+=1

	print ("RMSE: " + str(getRMSE(sqrtSum,count)))




if __name__ == "__main__" :
    netflixRatingPredictor()

