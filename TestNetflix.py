from io       import StringIO
from unittest import main, TestCase

import Netflix

from Netflix import getPredictedRating, getRealRating, getRMSE
# -----------
# TestCollatz
# -----------

class TestNetflix (TestCase) :
    # ----
    # get predicted Rating
    # ----
    
    def test_getPredictedRating_1 (self) :
        movieID    = "2684"
        userID     = "1"
        i = getPredictedRating(movieID,userID)
        print(i)

        self.assertTrue( 1 <= i <= 5)

    def test_getPredictedRating_2 (self) :
        movieID    = "5000"
        userID     = "1"
        i = getPredictedRating(movieID, userID)
        print(i)

        self.assertTrue(1 <= i <= 5)

    def test_getPredictedRating_3 (self) :
        movieID    = "6000"
        userID     = "1"
        i = getPredictedRating(movieID,userID)
        print(i)
        # should raise an exception for an out of range 
        #self.assertRaises(Exception, getPredictedRating, movieID)
        self.assertTrue(1 <= i <= 5)

    # ----
    # get Real Ratings
    # ----

    def test_getRealRatings_1 (self) :
        movieID    = '1234'
        userID     = '599906'
        
        #i =  float(answersCache[str(movieID)][str(userID)])
        i = getRealRating(movieID,userID)
        print("test_getRealRatings_1")
        print(i)
        #self.assertTrue(1 <= i <= 5)

    def test_getRealRating_2 (self) :
        movieID    = "5400"
        userID     = "2134385"
        i = getRealRating(movieID,userID)
        print(i)
        #self.assertTrue(1 <= i <= 5)
        """
    def test_getRealRating_3 (self) :
        movieID    = "18000\n"
        userID     = " 1\n"
        i = getRealRating(movieID,serI))
        print(i)
        #self.assertRaises(Exception, getRealRating, movieID)
        """

    

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
