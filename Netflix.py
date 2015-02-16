#!/usr/bin/env python3

import sys 
import json 
import fileinput
import math
import string

#limits provided  by project specs
CUSTOMER_ID_LIMIT = 2649429
MOVIE_ID_LIMIT = 17770

#recommended in the following article on the project page: http://www.science20.com/random_walk/predicting_movie_ratings_math_won_netflix_prize
OVERALL_MOVIE_RATINGS_AVG = 3.7


#List of movieID or userID that were not in out caches
numMisses = [0]

#A cache that holds a mapping between movie ID and an average of all ratings for this movie
movieRatingCache = json.load(open('pma459-mvAvgCache.json', 'r'))

#A cache that holds accurate ratings for each movie 
answersCache = json.load(open('pma459-answersCache.json', 'r'))

#A cache that holds a mapping between user/customer ID and an average rating it gives to movies in general
userAverageRatingCache = json.load(open('pma459-usrAvgCache.json', 'r'))

# -----------
# getPredictedRating
# -----------


def getPredictedRating(userID,movieID):
	"""
	TO DO : describe this when finished with the exact rating
	"""
	userID = int(userID)
	movieID = int(movieID)

	assert movieID >= 1 and movieID <= MOVIE_ID_LIMIT 

	movieAvgRating = float(movieRatingCache[movieID])
	userAvgRating = 0
	try:
		#we have data about the user
		userAvgRating = float(userAverageRatingCache[str(userID)])

		#yearlyDeviation = 3.228-movieYearCache[str(movieID)]
		#prediction = (overallAvg + (userAvgRating-(overallAvg))+ (movieAvgRating-(overallAvg)))
		prediction = userAvgRating  + movieAvgRating - OVERALL_MOVIE_RATINGS_AVG
		
		if(prediction < 1):
			prediction =1
		if(prediction > 5):
			prediction = 5
		return prediction

	except KeyError:
		#we dont have data about the user. so just use the average for that movie
		numMisses[0]+=1
		return movieAvgRating

# -----------
# getRealRating
# -----------	
def getRealRating(userID,movieID):
	"""
	It returns the actual rating that we want to get as close to. If the rating does not exist then we
	return a 0.
	"""
	userID = int(userID)
	movieID = int(movieID)

	assert movieID >=1  and movieID <= MOVIE_ID_LIMIT
	assert userID >= 1 and userID <= CUSTOMER_ID_LIMIT 	
	try:
		return float(answersCache[str(movieID)][str(userID)])
	except KeyError:
		return 0
	
# -----------
# getRMSE
# -----------	
def getRMSE(sqrtSum,numElements):
	"""
	Calculates the root mean squared error of a given sum of squared difference 
	and return a floating point round to two decimal points
	"""
	return round(((sqrtSum)/numElements)**0.5,2)

# -----------
# netflixRatingPredictor 
# -----------	
def netflixRatingPredictor():
	"""
	TODO: Describe this function in detail 
	"""
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

	print ("RMSE: " + str(getRMSE(sqrtSum,count)))
	print("misses: " + str(numMisses[0]))
	print("entries: " + str(count))



if __name__ == "__main__" :
	netflixRatingPredictor()




