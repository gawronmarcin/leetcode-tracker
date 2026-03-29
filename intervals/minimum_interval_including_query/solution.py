from typing import List
import random


"""
Task:
You are given a 2D integer array intervals, where intervals[i] = [left_i, right_i] represents the ith interval starting at left_i and ending at right_i (inclusive).

You are also given an integer array of query points queries. The result of query[j] is the length of the shortest interval i such that left_i <= queries[j] <= right_i. If no such interval exists, the result of this query is -1.

Return an array output where output[j] is the result of query[j].


Solution: Sweep Line + Custom Min-Heap (Offline Processing)

1. Sort: Intervals by start time, queries ascending (preserving original indices).
2. Sweep: Iterate through sorted queries. Add all newly started intervals (left <= query) to a custom Min-Heap, ordered by interval length.
3. Lazy Deletion: Continuously pop intervals from the top of the heap if they have already expired (right < query).
4. Result: The top of the heap now holds the shortest valid interval. If the heap is empty, return -1.

Note: The Min-Heap is built entirely from scratch using custom O(log K) operations (sift_up, heapify).

"""




def partition(T, p, r):
    x=random.randint(p,r)
    T[x],T[r]=T[r],T[x]
    pivot = T[r][0][0]
    i = p
    for j in range(p, r):
        if T[j][0][0] < pivot:
            T[i], T[j] = T[j],T[i]
            i += 1
    T[i], T[r] = T[r], T[i]
    return i


def quicksort(T, p, r):
    while p < r:
        q = partition(T, p, r)
        if ((q - 1) - p) > (r - (q + 1)):
            quicksort(T, q + 1, r)
            r = q - 1
        else:
            quicksort(T, p, q - 1)
            p = q + 1
def parent(x):
    return (x-1)//2
def left_child(x):
    return (2*x)+1
def right_child(x):
    return (2*x)+2
def heapify(T,x,n):
    mini=x
    if left_child(x) <n and T[left_child(x)][1] < T[x][1]:
        mini=left_child(x)
    if right_child(x) <n and T[right_child(x)][1] < T[mini][1]:
        mini=right_child(x)
    if mini!=x:
        T[mini],T[x] = T[x],T[mini]
        heapify(T,mini,n)

def sift_up(T, i):
    while i > 0:
        p = parent(i)
        if T[i][1] < T[p][1]:
            T[i], T[p] = T[p], T[i]
            i = p
        else:
            break

def miniInterval(intervals, queries):
    n = len(intervals)
    for i in range(n):
        intervals[i]=(intervals[i], intervals[i][1]-intervals[i][0]+1)
    quicksort(intervals, 0, n-1)
    for ind in range(len(queries)):
        queries[ind]=(queries[ind],ind)
    queries=sorted(queries)
    output=[0]*len(queries)
    print(intervals,queries)
    heap=[]
    i=0
    for query in queries:
        while i < n and intervals[i][0][0]<=query[0]:
            heap.append(intervals[i])
            sift_up(heap, len(heap) - 1)
            i += 1
        while len(heap) > 0 and heap[0][0][1] < query[0]:
            heap[0] = heap[-1]
            heap.pop()
            if len(heap) > 0:
                heapify(heap, 0, len(heap))
        if len(heap) > 0:
            output[query[1]] = heap[0][1]
        else:
            output[query[1]] = -1
    return output

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
       return miniInterval(intervals,queries)
