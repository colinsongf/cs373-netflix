#!/usr/bin/env python3

from io       import StringIO
from unittest import main, TestCase

import Netflix

from Netflix import getPredictedRating, getRealRating, getRMSE
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
        self.assertEqual(i, 6.93)

        
    def test_getRMSE_3 (self) :
        squareRootsum    = 40
        numElements     = 5
        i = getRMSE(squareRootsum,numElements)
        self.assertEqual(i, 2.83)

# ----
# main
# ----

if __name__ == "__main__" :
    main()
"""

% coverage3 run --branch TestCollatz.py >  TestCollatz.out 2>&1



% coverage3 report -m                   >> TestCollatz.out



% cat TestCollatz.out
.......
----------------------------------------------------------------------
Ran 7 tests in 0.001s

OK
Name          Stmts   Miss Branch BrMiss  Cover   Missing
---------------------------------------------------------
Collatz          18      0      6      0   100%
TestCollatz      33      1      2      1    94%   79
---------------------------------------------------------
TOTAL            51      1      8      1    97%

"""
