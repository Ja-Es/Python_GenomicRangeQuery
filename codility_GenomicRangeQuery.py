############################################################################### 
# My solution to the codility Task GenomicRangeQuery on 
# https://app.codility.com/programmers/lessons/5-prefix_sums/genomic_range_query/


#### TASK: 
# A DNA sequence of nucleotides (length N) is given. 
# Find the smallest impact factor of the nucleotides (A, C, G and T with 
# impact factors of 1, 2, 3 and 4, respectively) in certain DNA sub sequences.
# The DNA sub sequencesare given by P, a vector of starting indices 
# and Q, a vector of according end indices (both length M)

#### Solution:
# time complexity: O(N + M) 


############################################################################### 

# Definition of function

def solution(S, P, Q):
    
    ##------
    ## Preparation for minimal time complexity: count nucleotides.
    ## Create counting vectors for each nucleotide. If a nucleotide appears in
    ## the DNA sequence its counting vector counts +1 at the accoding index.
    
    # initialization of count-vectors
    countA = [0]*(len(S)+1)
    countC = [0]*(len(S)+1)
    countG = [0]*(len(S)+1)
    countT = [0]*(len(S)+1)
    results = [0]*len(P)
    
    # counting nucleotides.

    for ii in range(1,len(S)+1):

        if S[ii-1] == 'A':
            if ii == 0: 
                countA[ii] = countA[ii]+1
            else: countA[ii] = countA[ii-1]+1
        else:
            countA[ii] = countA[ii-1]
        
        if S[ii-1] == 'C':
            if ii == 0: 
                countC[ii] = countC[ii]+1
            else: countC[ii] = countC[ii-1]+1
        else:
            countC[ii] = countC[ii-1]
                    
        if S[ii-1] == 'G':
            if ii == 0: 
                countG[ii] = countG[ii]+1
            else: countG[ii] = countG[ii-1]+1
        else:
            countG[ii] = countG[ii-1]
        
        if S[ii-1] == 'T':
            if ii == 0: 
                countT[ii] = countT[ii]+1
            else: countT[ii] = countT[ii-1]+1
        else:
            countT[ii] = countT[ii-1]
            
            
    ##------
    ## Actual task: search "minimal nucleotide" in DNA sub sequences using 
    ## the counting vectors.      

    for jj in range(len(P)):

        if countA[Q[jj]+1]-countA[P[jj]]>0:
            results[jj] = 1
        elif countC[Q[jj]+1]-countC[P[jj]]>0:
            results[jj] = 2
        elif countG[Q[jj]+1]-countG[P[jj]]>0:
            results[jj] = 3
        elif countT[Q[jj]+1]-countT[P[jj]]>0:
            results[jj] = 4
            

    return results

# -----------------------------------------------------------------------------
# test of function with example from website

S=['C','A','G','C','C','T','A']
P=[2,5,0]
Q=[4,5,6]
    
print(solution(S,P,Q))