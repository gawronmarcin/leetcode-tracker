from typing import List

"""
Task:
You are given an 2-D array points where points[i] = [xi, yi] represents the coordinates of a point on an X-Y axis plane. You are also given an integer k.

Return the k closest points to the origin (0, 0).

The distance between two points is defined as the Euclidean distance (sqrt((x1 - x2)^2 + (y1 - y2)^2)).

You may return the answer in any order.

Solution:
Maintains a Max-Heap of size K to find the K closest points.

1. Calculates the squared Euclidean distance for each point to avoid expensive sqrt() operations.
2. Builds a Max-Heap with the first K points.
3. For the remaining points, if a point is closer than the furthest point currently in the heap (the root), it replaces the root and restores the heap property.

Time Complexity: O(N log K)
Space Complexity: O(K)
"""

def parent(x):
    return (x-1)//2
def left_child(x):
    return (2*x)+1
def right_child(x):
    return (2*x)+2
def push_down(T,x):
    n=len(T)
    left=left_child(x)
    right=right_child(x)
    if x<n:
        biggest=x
        if left<n:
            if T[left][1]>T[biggest][1]:
                biggest=left
        if right<n:
            if T[right][1]>T[biggest][1]:
                biggest=right
        if biggest!=x:
            T[biggest],T[x]=T[x],T[biggest]
            push_down(T,biggest)
def push_up(T,x):
    if x>0:
        if T[parent(x)][1]<T[x][1]:
            T[parent(x)],T[x]=T[x],T[parent(x)]
            push_up(T,parent(x))
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        for i in range(len(points)):
            points[i]=(points[i],((points[i][0]**2)+(points[i][1]**2)))
        maxheap=[]
        for i in range(len(points)):
            if len(maxheap)<k:
                maxheap.append(points[i])
                push_up(maxheap,len(maxheap)-1)
            else:
                if maxheap[0][1]>points[i][1]:
                    maxheap[0]=points[i]
                    push_down(maxheap,0)
        for i in range(len(maxheap)):
            maxheap[i]=maxheap[i][0]
        return maxheap