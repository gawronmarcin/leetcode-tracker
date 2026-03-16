import sys
from random import randint, seed

OIOIOI = False

"""
Task:
Given an n-element array of words T. For each index i < n, the domination 
coefficient of the word at position i is defined as the number of words that 
appear in the array before the i-th element and are lexicographically smaller 
than T[i].

Lexicographical order: Word A is lexicographically greater than word B, if:
1. At the first position i where these words differ (A[i] != B[i]), the 
   character A[i] appears later in the alphabet than the character B[i]. 
   This means that the word 'kwiatek' is lexicographically greater than the 
   word 'auto', and the word 'dym' is lexicographically greater than 'domek'.
2. If B is a prefix of A. This means that the word 'autostrada' is 
   lexicographically greater than the word 'auto', and the word 'drogowskaz' 
   is lexicographically greater than 'drogo'.

Word A is lexicographically smaller than word B if A != B and A is not 
lexicographically greater than B.

Please complete the body of the function solution(T), which for an array T 
containing n words will return the maximum domination coefficient among all 
words in the array.
"""

"""
Solution:
I sort the array in lexicographical order using merge sort.
During the merge step, I count how many words each element dominates 
(i.e., how many words from the left sub-array are lexicographically smaller).
Finally, I return the maximum domination coefficient found.

"""

def merge(A,B,p,q,r,counter): # Merges two sorted halves of the array.
    i=p
    left=p
    middle=q
    right=r
    while p<middle and q<right: # Compares elements from both halves and places them into the buffer array in order.
        if A[p][1]<A[q][1]:
            B[i]=A[p]
            p+=1
        else:
            counter[A[q][0]] += (p-left)
            B[i]=A[q]
            q+=1
        i+=1
    if p<middle: # Puts the remaining elements into the buffer array.
        while p<middle:
            B[i]=A[p]
            p+=1
            i+=1
    if q<right:
        while q<right:
            counter[A[q][0]] += middle-left
            B[i]=A[q]
            q+=1
            i+=1
    for j in range(left,right): # Copies the buffer array back into array A.
        A[j]=B[j]
def merge_sort(A,B,p,r,counter): # Sorts the array by recursively merging sorted left and right halves.
    if r-p<=1: # If the part being sorted contains one element, it's already sorted.
        return A
    q=(p+r)//2
    merge_sort(A,B,p,q,counter)
    merge_sort(A,B,q,r,counter)
    merge(A,B,p,q,r,counter)
    return A



def solution(T):
    n=len(T)
    counter=[0]*n # Array to count the domination coefficient for the word at each original index.
    A=[0]*n # Array of tuples where the first value is the original index and the second is the word.
    for i in range(n):
        A[i]=(i,T[i])
    B = [0]*n # Buffer array for merge sort.
    merge_sort(A,B,0,n,counter)
    maxi=-1
    for j in range(len(counter)):
        if counter[j]>maxi:
            maxi=counter[j]
    return maxi
if __name__ == "__main__":
    def generate_random_string(length):
        return ''.join(chr(randint(97, 122)) for _ in range(length))


    if OIOIOI:
        n = int(sys.stdin.readline().strip())
        words = [sys.stdin.readline().strip() for _ in range(n)]
        print(solution(words))
    else:
        seed(1)
        test_def = [
            (10, 5, 10, 6),
            (100, 5, 10, 88),
            (100, 20, 100, 91),
            (10000, 10, 30, 9901)
        ]
        ok = 0
        for idx, (n, m_low, m_high, ans) in enumerate(test_def):
            print("Test", idx + 1)
            words = [generate_random_string(randint(m_low, m_high)) for _ in range(n)]
            result = solution(words)
            if result == ans:
                print("OK")
                ok += 1
            else:
                print("Błąd!")
        print("Wynik:", ok, "/", len(test_def))