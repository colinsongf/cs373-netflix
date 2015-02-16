import json
import fileinput 
import string
import collections

movieRatingCache = json.load(open('yearToMovie.json', 'r'))
yearMovieCache = json.load(open('yearlyMovieCache.json'),'r')

def sameple():
	#for each movie ID there is a year
	sorted_x = collections.OrderedDict(sorted(movieRatingCache.items()))
	print (sorted_x)
if __name__ == "__main__" :
	sample()