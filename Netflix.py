#!/usr/bin/env python3

import sys 
import json 
import fileinput


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

#A cache that holds a mapping between user/customer ID and the ratings he gives for each decade
userDecadeAverageCache = json.load(open('cdm2697-userRatingsAveragedOver10yInterval.json', 'r'))

#A cache that holds a mapping between movie and year
movieYearCache = json.load(open('af22574-movieDates.json'))

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
		userAvgRating = float(userAverageRatingCache[str(userID)])
		year = 0
		try:
			year = int(movieYearCache[str(movieID)])
			assert(year>=1890)
			assert(year<=2010)
			ratingsList = userDecadeAverageCache[str(userID)]
			if(year>=1890 and year<1900):
				found = False
				for triplet in ratingsList:
					if("1890" in triplet[0]):
						userAvgRating = float(triplet[1])
						found = True
						break
				if(not found):
					print("did not find entry for movieID: " + str(movieID) + ", userID: " + str(userID) + ", year: " + str(year) )
			elif(year<1910):
				found = False
				for triplet in ratingsList:
					if("1900" in triplet[0]):
						userAvgRating = float(triplet[1])
						found = True
						break
				if(not found):
					print("did not find entry for movieID: " + str(movieID) + ", userID: " + str(userID) + ", year: " + str(year) )
			elif(year<1920):
				found = False
				for triplet in ratingsList:
					if("1910" in triplet[0]):
						userAvgRating = float(triplet[1])
						found = True
						break
				if(not found):
					print("did not find entry for movieID: " + str(movieID) + ", userID: " + str(userID) + ", year: " + str(year) )
			elif(year<1930):
				found = False
				for triplet in ratingsList:
					if("1920" in triplet[0]):
						userAvgRating = float(triplet[1])
						found = True
						break
				if(not found):
					print("did not find entry for movieID: " + str(movieID) + ", userID: " + str(userID) + ", year: " + str(year) )
			elif(year<1940):
				found = False
				for triplet in ratingsList:
					if("1930" in triplet[0]):
						userAvgRating = float(triplet[1])
						found = True
						break
				if(not found):
					print("did not find entry for movieID: " + str(movieID) + ", userID: " + str(userID) + ", year: " + str(year) )
			elif(year<1950):
				found = False
				for triplet in ratingsList:
					if("1940" in triplet[0]):
						userAvgRating = float(triplet[1])
						found = True
						break
				if(not found):
					print("did not find entry for movieID: " + str(movieID) + ", userID: " + str(userID) + ", year: " + str(year) )
			elif(year<1960):
				found = False
				for triplet in ratingsList:
					if("1950" in triplet[0]):
						userAvgRating = float(triplet[1])
						found = True
						break
				if(not found):
					print("did not find entry for movieID: " + str(movieID) + ", userID: " + str(userID) + ", year: " + str(year) )
			elif(year<1970):
				found = False
				for triplet in ratingsList:
					if("1960" in triplet[0]):
						userAvgRating = float(triplet[1])
						found = True
						break
				if(not found):
					print("did not find entry for movieID: " + str(movieID) + ", userID: " + str(userID) + ", year: " + str(year) )
			elif(year<1980):
				found = False
				for triplet in ratingsList:
					if("1970" in triplet[0]):
						userAvgRating = float(triplet[1])
						found = True
						break
				if(not found):
					print("did not find entry for movieID: " + str(movieID) + ", userID: " + str(userID) + ", year: " + str(year) )
			elif(year<1990):
				found = False
				for triplet in ratingsList:
					if("1980" in triplet[0]):
						userAvgRating = float(triplet[1])
						found = True
						break
				if(not found):
					print("did not find entry for movieID: " + str(movieID) + ", userID: " + str(userID) + ", year: " + str(year) )
			elif(year<2000):
				found = False
				for triplet in ratingsList:
					if("1990" in triplet[0]):
						userAvgRating = float(triplet[1])
						found = True
						break
				if(not found):
					print("did not find entry for movieID: " + str(movieID) + ", userID: " + str(userID) + ", year: " + str(year) )
			elif(year<2010):
				found = False
				for triplet in ratingsList:
					if("2000" in triplet[0]):
						userAvgRating = float(triplet[1])
						found = True
						break
				if(not found):
					print("did not find entry for movieID: " + str(movieID) + ", userID: " + str(userID) + ", year: " + str(year) )
				

		except Exception as e:
			print(e)
			print("exception raised for userID: " + str(userID) + ", movieID: " + str(movieID))
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

# ------------
# collatz_read
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




