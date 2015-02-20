#!/usr/bin/env python3

from io       import StringIO
from unittest import main, TestCase

from Netflix import getPredictedRating, getRealRating, getRMSE, netflixRead, netflixPrint , netflixSolve
# -----------
# TestNetflix
# -----------

class TestNetflix (TestCase) :
    # ----
    # get predicted Rating
    # ----
    def test_getPredictedRating_1 (self) :
        movieID    = "2684"
        userID     = 1
        i = getPredictedRating(movieID,userID)
        self.assertTrue(1 <= i <= 5)

    def test_getPredictedRating_2 (self) :
        movieID    = "wdfasdf"
        userID     = "1"
        self.assertRaises(ValueError,getPredictedRating,movieID,userID)

    def test_getPredictedRating_3 (self) :
        movieID    = "6000"
        userID     = "0"
        self.assertRaises(AssertionError,getPredictedRating,movieID,userID)
       
     # ----
     # get Real Ratings
     # ----

    def test_getRealRatings_1 (self) :
        movieID    = '1234'
        userID     = '599906'
        i = getRealRating(userID,movieID)
        self.assertTrue(1 <= i <= 5)

    def test_getRealRating_2 (self) :
        #look for an entry that does not exist.
        movieID    = "5400"
        userID     = "0"
        self.assertRaises(AssertionError,getRealRating,userID,movieID)

        
    def test_getRealRating_3 (self) :
        movieID    = "1800"
        userID     = "lol\n"
        self.assertRaises(ValueError,getRealRating,userID,movieID)

    def test_getRealRating_4 (self) :
        movieID    = "1234"
        userID     = "1234"
        i = getRealRating(userID,movieID)
        self.assertTrue(i == 0)

    # ----
    # Calculate Root Mean Squared Error
    # ----
    def test_getRMSE_1 (self) :
        squareRootsum    = 0.358302
        numElements     = 7
        i = getRMSE(squareRootsum,numElements)
        self.assertEqual(i, 0.23)

    def test_getRMSE_2 (self) :
        squareRootsum    = 97
        numElements     = 2
        i = getRMSE(squareRootsum,numElements)
        self.assertEqual(i, 6.96)

        
    def test_getRMSE_3 (self) :
        squareRootsum    = 40
        numElements     = 5
        i = getRMSE(squareRootsum,numElements)
        self.assertEqual(i, 2.83)

    def test_getRMSE_4 (self) :
        squareRootsum    = 100
        numElements     = 100
        i = getRMSE(squareRootsum,numElements)
        self.assertEqual(str(i), "1.00")


    # ----
    # Reading
    # ----
    def test_netflixRead1 (self) :
        line = "1:\n"
        returnValue = netflixRead(line)
        self.assertEqual(returnValue[0], True)
        self.assertEqual(returnValue[1], "1")

    def test_netflixRead2 (self) :
        line = "2:\n"
        returnValue = netflixRead(line)
        self.assertEqual(returnValue[0], True)
        self.assertEqual(returnValue[1], "2")

    def test_netflixRead3 (self) :
        line = "30878\n"
        returnValue = netflixRead(line)
        self.assertEqual(returnValue[0], False)
        self.assertEqual(returnValue[1], "30878")


    # ----
    # Reading
    # ----

    def test_netflixPrint1 (self) :
        w = StringIO()
        s = "5.34"
        t = False
        netflixPrint(w,s,t)
        self.assertEqual(w.getvalue(), "5.3\n")

    def test_netflixPrint2 (self) :
        w = StringIO()
        s = 1.23
        t = False
        netflixPrint(w,s,t)
        self.assertEqual(w.getvalue(), "1.2\n")

    def test_netflixPrint3 (self) :
        w = StringIO()
        s = "1"
        t = True
        netflixPrint(w,s,t)
        self.assertEqual(w.getvalue(), "1:\n")


    # ----
    # Netflix Solve 
    # ---

    def test_netflixsolve1 (self) :
        r = StringIO("1:\n30878\n2647871\n1283744\n2488120\n317050\n1904905\n1989766\n14756\n1027056\n1149588\n1394012\n1406595\n2529547\n1682104\n2625019\n2603381\n1774623\n470861\n712610\n1772839\n1059319\n2380848\n548064\n")
        w = StringIO()
        RMSE = netflixSolve(w,r)
        self.assertTrue(RMSE < 1)

    def test_netflixsolve2 (self) :
        r = StringIO("10:\n1952305\n1531863")
        w = StringIO()
        RMSE = netflixSolve(w,r)
        self.assertTrue(RMSE < 1)

    def test_netflixsolve3 (self) :
        r = StringIO("1000:\n2326571\n977808\n1010534\n1861759\n79755\n98259\n1960212\n97460\n2623506\n2409123\n1959111\n809597\n2251189\n537705\n929584\n506737\n708895\n1900790\n2553920\n1196779\n2411446\n1002296\n1580442\n100291\n433455\n2368043\n906984\n10008:\n1813636\n2048630\n930946\n1492860\n1687570\n1122917\n1885441\n10009:\n1927533\n1789102\n2263612\n964421\n701514\n2120902\n")
        w = StringIO()
        RMSE = netflixSolve(w,r)
        self.assertTrue(RMSE < 1)
    
# ----
# main
# ----

if __name__ == "__main__" :
    main()
