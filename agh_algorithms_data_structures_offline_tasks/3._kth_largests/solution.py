import sys
import array

"""
Problem:
We have an array T of length n and q queries. For each query 1 <= q_i <= n, 
you need to output the q_i-th largest number in the array T.

Solution notes:
This code is strictly optimized to pass tight Memory Limits (MLE) in Python:
1. Input: Uses a generator to read sys.stdin stream token by token, 
   avoiding loading the massive input file into RAM all at once.
2. Data structure: Uses the 'array' module (C-style raw integers) instead 
   of standard Python lists to drastically reduce object memory overhead.
3. Sorting: Custom in-place 3-way QuickSort (Dutch National Flag) ensures 
   O(1) extra memory space, as no subarrays are allocated during sorting.
"""

def partition(T,p,r):
    mid = (p + r) // 2
    pivot = T[mid]
    i=p
    s=p
    t=r
    while i<=t:
        if T[i]>pivot:
            T[s],T[i]=T[i],T[s]
            s+=1
            i+=1
        elif T[i]<pivot:
            T[i],T[t]=T[t],T[i]
            t-=1
        else:
            i+=1
    return s,t

def quicksort(T,p,r):
    while p < r:
        s, t = partition(T, p, r)
        if (s - p) < (r - t):
            quicksort(T, p, s - 1)
            p = t + 1

        else:
            quicksort(T, t + 1, r)
            r = s - 1

class Solution:
    def solve(self):
        def get_ints():
            for line in sys.stdin:
                for token in line.split():
                    yield int(token)

        iterator = get_ints()

        try:
            n = next(iterator)
        except StopIteration:
            return

        T = array.array('i', (next(iterator) for _ in range(n)))

        q = next(iterator)
        zapytania = array.array("i", (next(iterator) for _ in range(q)))

        quicksort(T, 0, n - 1)

        for zap in zapytania:
            print(T[zap - 1])


if __name__ == '__main__':
    Solution().solve()