#!/usr/bin/env python3

import Netflix


movieID = "lol"
userID = "2"
# try:
# 	i = Netflix.getPredictedRating(movieID,userID)
# 	print(i)
# except TypeError as e:
# 	print(e)
# 	print(type(e))
# 	print("caught error")
# else:
# 	pass

try:
	Netflix.getPredictedRating(movieID,userID)
except Exception as e:
	print(e)
	print(type(e))

