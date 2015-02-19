#!/usr/bin/env python3

import sys 
import json 
import fileinput


#limits provided  by project specs
CUSTOMER_ID_LIMIT = 2649429
MOVIE_ID_LIMIT = 17770

#recommended in the following article on the project page: http://www.science20.com/random_walk/predicting_movie_ratings_math_won_netflix_prize
OVERALL_MOVIE_RATINGS_AVG = 3.7


#List of movieID or userID that were not in out caches. 0-noYear 1-noDecade 2-noUserData
numMisses = [0,0,0]

#A cache that holds a mapping between movie ID and an average of all ratings for this movie
movieRatingCache = json.load(open('/u/mck782/netflix-tests/pma459-mvAvgCache.json', 'r'))

#A cache that holds accurate ratings for each movie 
answersCache = json.load(open('/u/mck782/netflix-tests/pma459-answersCache.json', 'r'))

#A cache that holds a mapping between user/customer ID and an average rating it gives to movies in general
userAverageRatingCache = json.load(open('/u/mck782/netflix-tests/pma459-usrAvgCache.json', 'r'))

#A cache that holds a mapping between user/customer ID and the ratings he gives for each decade
userDecadeAverageCache = json.load(open('/u/mck782/netflix-tests/cdm2697-userRatingsAveragedOver10yInterval-v2.json', 'r'))

#A cache that holds a mapping between movie and year
movieYearCache = json.load(open('/u/mck782/netflix-tests/af22574-movieDates.json'))

# -----------
# getPredictedRating
# -----------


def getPredictedRating(userID,movieID):
	"""
	userID the id of the user
	movieID the id of the movie
	returns a predicted a rating based on our algorithm. It is based on the movie average, and how the user feels about movies within that decade
	"""
	userID = int(userID)
	movieID = int(movieID)

	assert movieID >= 1 and movieID <= MOVIE_ID_LIMIT 

	#the key parameters to our algorithm
	movieAvgRating = 0
	userAvgRating = 0
	year = 0

	#get the overall average of that movie
	movieAvgRating = float(movieRatingCache[movieID])
	assert (type(movieAvgRating)==float)

	#find the year of the movie. If we dont have it then make userAvgRating just the average. If we dont have any info about that user, then use the movieAverage
	foundYear = False
	try:
		year = int(movieYearCache[str(movieID)]) ##if we cant the year of the movie, then just return the average rating
		assert(year>=1890)
		assert(year<=2010)
		foundYear = True
	except Exception:
		numMisses[0]+=1
		if(str(userID) in userAverageRatingCache):
			userAvgRating = float(userAverageRatingCache[str(userID)])
		else:
			userAvgRating = movieAverage
			numMisses[2]+=1

	#find the avg rating for that decade. If we cant find it, just assign the regular user average, if thats not possible, then just the movieAverage
	
	if(str(userID) in userDecadeAverageCache and foundYear ):
		ratingsList = userDecadeAverageCache[str(userID)]
		decade = int(year/10)*10
		assert(decade>=1890 and decade<=2000)
		foundDecade = False
		for triplet in ratingsList :
			if(triplet[0] ==  decade):
				userAvgRating = triplet[1]
				foundDecade = True
				break
		if(not foundDecade):
			numMisses[1]+=1
			if(str(userID) in userAverageRatingCache):
				userAvgRating = float(userAverageRatingCache[str(userID)])
			else:
				userAvgRating = movieAverage
				numMisses[2]+=1
			

	prediction = userAvgRating  + movieAvgRating - OVERALL_MOVIE_RATINGS_AVG
		
	if(prediction < 1):
		prediction =1
	elif(prediction > 5):
		prediction = 5
	return prediction

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

# ------------
# netflixRead
# ------------
def netflixRead (s) :
	"""
	s a string
	parse a line in the input and see if its either a movieID or a rating.
   	If it is a movieID return (True,movieID); if it is a userID, return (False,userID)
	"""

	if ":" in s:
		return (True,s.split(":")[0])
	else:
		return (False,s.rstrip())

# -----------
# netflixPrint 
# -----------	

def netflixPrint (w, s, t) :
    """
    print three ints
    w a writer
    s the number to print
    t a boolean flag indicating if a movieID(True) or a userID(False) should be printed
    """


    if(t):
    	w.write(str(s)+":\n")
    else:
    	s = round(float(s),1)
    	w.write(str(s)+"\n")

# -----------
# netflixRatingPredictor 
# -----------	
def netflixSolve(w,r):
	"""
    r a reader
    w a writer
    """
	#read in a line
	movieID = ""
	sqrtSum = 0
	count = 0
	for line in r:
		isMovieID,id = netflixRead(line)
		if isMovieID:
			#we have a new movie
			movieID = id
			netflixPrint(w,movieID,True)
		else:
			#we are predicting the rating userID gave to movieID
			userID = id
			predictedRating = getPredictedRating(int(userID),int (movieID))
			realRating = getRealRating(userID,movieID)
			diff = predictedRating - realRating
			sqrtSum += diff **2
			count+=1
			netflixPrint(w,predictedRating,False)

	RMSE = getRMSE(sqrtSum,count)
	w.write("RMSE: " + str(RMSE) + "\n")
	return RMSE

