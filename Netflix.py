#!/usr/bin/env python3

import sys 
import json 
import fileinput
import math
import string

CUSTOMER_ID_LIMIT = 2649429
MOVIE_ID_LIMIT = 17770
overallAvg = 3.623

numMisses = [0]

movieRatingCache = json.load(open('movieAverageCache.json', 'r'))
answersCache = json.load(open('pma459-answersCache.json', 'r'))
userAverageRatingCache = json.load(open('pma459-usrAvgCache.json', 'r'))
movieYearCache = json.load(open('yearlyMovieCache.json','r'))
yearAverageCache = json.load(open('yearAverageCache.json','r'))

def netflix_cache_gen (cache, fileObject):
    """
    cache is a pointer to the list to build the cache in
    fileObject is the input cache file
    returns parsed list
    """    
    for line in fileObject: 
        line = line.strip()
        (itemID, rating) = line.split(" ")
        assert int(itemID) >= 1 and int(itemID) <= 2649429
        assert float(rating) >= 1.0 and float(rating) <= 5.0
        cache[int(itemID)] = float(rating)
    fileObject.close()

def getPredictedRating(userID,movieID):
	userID = int(userID)
	movieID = int(movieID)
	assert movieID >= 1 and movieID <= MOVIE_ID_LIMIT 

	movieAvgRating = float(movieRatingCache[str(movieID)])
	userAvgRating = 0
	try:
		#we have data about the user
		userAvgRating = float(userAverageRatingCache[str(userID)])
<<<<<<< HEAD
		#year = movieYearCache[str(movieID)]
		#yearAverage = float(yearAverageCache[year])
		#yearlyDeviation = 3.228-movieYearCache[str(movieID)]
		return (overallAvg + (userAvgRating-overallAvg)+ (movieAvgRating-overallAvg))
	except KeyError as e:
=======
		year = movieYearCache[str(movieID)]
		yearAverage = float(yearAverageCache[year])
		overallAvg = 3.623
		#yearlyDeviation = 3.228-movieYearCache[str(movieID)]
		#prediction = (overallAvg + (userAvgRating-(overallAvg))+ (movieAvgRating-(overallAvg)))
		prediction = userAvgRating + movieAvgRating - overallAvg
		if(prediction < 1):
			prediction =1
		if(prediction > 5):
			prediction = 5

		return prediction


	except KeyError:
>>>>>>> b128fb13463b210f397503e19739efe63ad005e5
		#we dont have data about the user. so just use the average for that movie
		numMisses[0]+=1
		print("missed: " + str(movieID) + " or " + str(userID))
		print("KeyError: " + str(e) )
		return movieAvgRating
	
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
			realRating = getRealRating(userID,movieID)
			diff = predictedRating - realRating
			sqrtSum += diff **2
			count+=1

	print("RMSE: " + str(getRMSE(sqrtSum,count)))
	print("misses: " + str(numMisses[0]))
	print("entries: " + str(count))



if __name__ == "__main__" :
	netflixRatingPredictor()


