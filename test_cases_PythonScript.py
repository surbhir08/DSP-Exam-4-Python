"""
This is a test script for all the functions from PythonScript.py file, when run using the command line, 
outputs the successful test as a check to see if functions run correctly.

Usage: test.py
"""
import pandas as pd
from PythonScript import *

"""
Test cases for running 1st function for returning possible kmers count.

test1 function returns positive test case
test2 function returns negative test case.

"""

def test1_get_possible_kmercount():      # py test function
  Seq = 'ATTTGGATT'                      # sequence (argument)
  k = 9                                  # k value (argument)
  actual_result = get_kmercount(Seq,k)   # getting actual results from main function for running test case
  expected_result = 1                    # as per test the result should be 1
  assert actual_result==expected_result  # matching actual results with the expected result to check if the function runs well.
  
def test2_get_possible_kmercount():      # py test function
  Seq = 'ATTTGGATT'                      # sequence (argument)
  k = -1                                 # k value (argument) -1 is not an appropriate value as we have used defensive coding for - values.
  actual_result = get_kmercount(Seq,k)   # getting actual results from main function for running test case
  expected_result = 8                    # as per test the result should be 8
  assert actual_result==expected_result  # matching actual results with the expected result to check if the function runs well.
  
#***********************************************************************************************************************************

"""
Test cases for running 2nd function for returning observed kmers count.

test1 function returns positive test case
test2 function returns positive test case.

"""
def test1_get_observed_kmercount():     # py test function
  Seq = 'ATTTGGATT'                     # sequence passed
  k = 8                                 # k value argument
  actual_result = get_obs_kmer(Seq,k)   #getting actual results from main function for running test case
  expected_result = 2                   #as per test the result should be 2
  assert actual_result==expected_result #matching actual results with the expected result to check if the function runs well.
  
def test2_get_observed_kmercount():     # py test function
  Seq = 'ATTTGGATT'                     # sequence passed
  k = 5                                 # k value argument
  actual_result = get_obs_kmer(Seq,k)   #getting actual results from main function for running test case
  expected_result = 5                   #as per test the result should be 5
  assert actual_result==expected_result #matching actual results with the expected result to check if the function runs well.

#***********************************************************************************************************************************

"""

Test cases for running 3rd function for returning Linguistic complexity of the sequence passed.

test1 function returns positive test case
test2 function returns positive test case.

"""
def test1_linguistic_complexity():            #function to py test 
  Seq = 'ATTTGGATT'                           #sequence 
  actual_result = linguistic_complexity(Seq)  #getting actual results from main function for running test case
  expected_result = 0.875                     #as per test the result should be 0.875
  assert actual_result==expected_result       #matching actual results with the expected result to check if the function runs well.
  
def test2_linguistic_complexity():            #function to py test
  Seq = 'APLKHHGT'                            #sequence
  actual_result = linguistic_complexity(Seq)  #getting actual results from main function for running test case
  expected_result = 1.09375                   #as per test the result should be 1.09375
  assert actual_result==expected_result       #matching actual results with the expected result to check if the function runs well.


#***********************************************************************************************************************************

"""
Test cases for running 4th function for checking dataframe function.

test1 function returns positive test case
test2 function returns positive test case.
"""

def test1_df():                                   #function to py test
  data = [[1,5,4],[2,7,8],[3,7,7],[4,6,6],[5,5,5],[6,4,4],[7,3,3],[8,2,2],[9,1,1]]  #expected data output
  expected_result = pd.DataFrame(data, columns = ['k', 'Observed kmers', 'Possible kmers'], index = [0,1,2,3,4,5,6,7,8])  #aligning the expected data into a data frame
  Seq = 'PHHATHAAG'                               # sequence passed
  actual_result = create_kmer_df(Seq)             # caling the main dataframe function to get the actual result
  result = expected_result.equals(actual_result)  #equting the expected and actual data outputs
  assert result == True                           #checking if the result is true
  
def test2_df():                                    #function to py test
  data = [[1,4,4],[2,4,4],[3,3,3],[4,2,2],[5,1,1]] #expected data output
  expected_result = pd.DataFrame(data, columns = ['k', 'Observed kmers', 'Possible kmers'], index = [0,1,2,3,4])    #aligning the expected data into a data frame
  Seq = 'AGGTH'                                     # sequence passed
  actual_result = create_kmer_df(Seq)               # caling the main dataframe function to get the actual result
  result = expected_result.equals(actual_result)    #equting the expected and actual data outputs
  assert result == True                             #checking if the result is true

