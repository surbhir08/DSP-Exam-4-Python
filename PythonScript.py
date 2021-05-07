"""
This script, when run using the command line, outputs the linguistic complexity of each
sequence in a file of sequences. The file will be specified by the end user as a command line
argument. main function at the bottom.

Usage: PythonScript.py <filename.txt>
"""
import pandas as pd
import sys 
import argparse

def get_kmercount(Seq,k): 
  """
    Summary : The function Counts the kmers of size k, where k is specified as an argument.
    
    description: This function takes k and a sequence Seq as input arguments and determines the number of possible k-mers 
    for a particular k-value
    
    Parameters: 
    Seq: the input sequence for which the number of k-mers need to be determined
    k: the input value, ranges from 1 to length of the sequence 
    
    Return:
    lk_pos: the number of kmers possible
  """
  lk_pos = []                              #empty list to contain kmers
  if k == 1:
    return 4;
  else:
    for i in range(0,len(Seq)-k+1):        #parsing through length of sequence passes and appending in the empty list declared before
      lk_pos.append(Seq[i:i+k])
    return(len(lk_pos))                    #returning the length of list as it will be the numbers of kmers possible.
"""
def main(args):                            #main function to run the function for returning number of possible kmers.
  assert args.k >= 0
  lk_pos=get_kmercount(args.Seq, args.k)   #calling the function get_kcount
  print(lk_pos)                            #print returned value.

if __name__=='__main__':                   #command for running the main module
  parser = argparse.ArgumentParser()
  parser.add_argument('Seq', type = str)
  parser.add_argument('k', type = int)
  args = parser.parse_args()
  main(args)
"""  
##############################################################################################################################

def get_obs_kmer(Seq,k):
  """
    Summary: Counts the number of observed kmers for a sequence, for a specific k value
    
    Description: This function takes k and a sequence Seq as input arguments and determines the number of observed k-mers 
    for a particular k-value
    
    Parameters: 
    Seq: the input sequence for which the k-mers need to be determined
    k: the input value, ranges from 1 to length of sequence 
    
    Return:
    lk_obs: the number of kmers observed
  """
  
  lk_pos = []                          #empty list for containing possible kmers  
  lk_obs = []                          #empty list for containing observed kmers
  count = 0                            #initializing count to 0
  length = len(Seq)                    #using python len function for getting the length of sequence passed
  
  for i in range (0,length-k+1):       #looping through 0 to length of the sequence-k value +1
    lk_pos.append(Seq[i:i+k])          # appending the ith to i+k index of sequence passed to list of possible kmers
    
    for item in lk_pos:                #looping through items in possible kmers list
      if item not in lk_obs:           # if it the item is not available in observed kmers list then increasing the count by 1 and appending the item to observed list
        count+=1
        lk_obs.append(item)
  return(count)                         #returning the total count
"""  
def main(args):                         #main function to run the function for returning number of observed kmers count.
  assert args.k >= 0                    # defensive code to make sure the value of k passed should be >= 0
  count=get_obs_kmer(args.Seq, args.k)  #calling the function
  print(count)                          #print returned count value.

if __name__=='__main__':                #command for running the main module
  parser = argparse.ArgumentParser()
  parser.add_argument('Seq', type = str)
  parser.add_argument('k', type = int)
  args = parser.parse_args()
  main(args)
  
"""
############################################################################################################################

def create_kmer_df(Seq):
  """
    Summary: Creates a data frame with k values, associated number of observed number of kmers and all possible number of kmers as columns. 
    
    Description: This function takes a sequence Seq as input argument and returns a pandas data frame 
    which has columns k value, observed kmer count and possible kmer count.
    
    Parameters: 
    Seq: the input sequence for which the kmer data frame needs to be created
    
    Return:
    kmer_df: kmer data frame
    """

  k = []                                 # initialized empty list for k values
  k_pos_list = []                        # initialized empty list for possible kmer values
  k_obs_list = []                        # initialized empty list for observed kmer values
  k = list(range(1,len(Seq)+1))          # initialising list k as have values from 1 to length of sequence passed + 1

  for i in k:                            # looping through values in list k
    k_pos = get_kmercount(Seq,i)         # calling function get_kmercount() to count possible kmers
    k_pos_list.append(k_pos)             # and appending in list of possible values

  for i in k:                            # looping through values in list k
    k_obs = get_obs_kmer(Seq,i)          # calling function get_obs_kmer() to count observed kmers values
    k_obs_list.append(k_obs)             # and appending in list of observed values

  kmer_df = pd.DataFrame(                # creating pandas the data frame using pd.DataFrame function
  {
    'k':k,                               # mapping the values to resoective columns of the dataframe
    'Observed kmers':k_obs_list,
    'Possible kmers':k_pos_list
  }
  )
  return kmer_df                         # returning data frame
"""  
def main(args):                          # main function to run the function for returning dataframe.
  kmer_df=create_kmer_df(args.Seq)       # calling the function
  print(kmer_df)                         # print returned value.

if __name__=='__main__':                 # command for running the main module
  parser = argparse.ArgumentParser()
  parser.add_argument('Seq', type = str)
  args = parser.parse_args()
  main(args)
"""
#############################################################################################################################

def linguistic_complexity(Seq):
  """
    Summary: Calculates the lingusitic complexity of a given sequence
    
    Description: This function takes a sequence Seq as input argument and produces the linguistic complexity, 
    the proportion of k-mers that are observed compared to the total number that are theoretically possible
        
    Parameters: 
    Seq: the input sequence for which the linguistic complexity needs to be determined
    
    Return:
    lc: linguistic complexity
  """

  kmer_df = create_kmer_df(Seq)                 #calling create dataframe function for forming dataframe
  tot_obs_kmer = sum(kmer_df['Observed kmers']) #addition of the values in observed kmers column
  #print (sum(kmer_df['Observed kmers']))
  tot_pos_kmer = sum(kmer_df['Possible kmers']) # addition of values in the possible kmers column
  #print (sum(kmer_df['Possible kmers']))
  lc = tot_obs_kmer/tot_pos_kmer                # formula of lc = sum of observed value/ sum of possible values
  return lc                                     # returning LC

"""
def main(args):                                 #main function to run the function for returning liguistic complexity.
  lc=linguistic_complexity(args.Seq)            #calling the function
  print(lc)                                     #print returned value.

if __name__=='__main__':                        #command for running the main module
  parser = argparse.ArgumentParser()
  parser.add_argument('Seq', type = str)
  args = parser.parse_args()
  main(args)
  
"""

if __name__=='__main__':
    
    myfile = sys.argv[1]
    with open(myfile,'r') as current_file:
        text = current_file.read()
    seq = text.split()                             # split sequences
    for i in range(0,len(seq)):
        #print(seq[i])
        lc_seq = linguistic_complexity(seq[i])
        print(lc_seq)                              # print the linguistic complexity

