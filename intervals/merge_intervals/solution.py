from typing import List
"""
Task:
Given an array of intervals where intervals[i] = [start_i, end_i], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

Solution:
1. Since interval start values are small (0 <= start <= 1000), use Counting Sort 
to sort the intervals by their start times in O(n) time.
2. Iterate through the sorted intervals keeping track of the current merged boundary ('end').
3. If the current interval overlaps with the boundary (start <= end), expand the boundary.
Otherwise, append the new interval to the result and update the boundary.
"""


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        counting = [0] * 1001

        # Counting frequencies of start times
        for interval in intervals:
            counting[interval[0]] += 1

        # Cumulative sum for stable sorting positions
        for i in range(1, len(counting)):
            counting[i] = counting[i - 1] + counting[i]

        srt = [0] * n

        # Placing intervals in sorted order
        for interval in intervals:
            counting[interval[0]] -= 1
            srt[counting[interval[0]]] = interval

        end = srt[0][1]
        intcount = 0
        res = []
        res.append(srt[0])

        # Linear merge
        for interval in srt:
            if interval[0] <= end:
                res[intcount][1] = max(end, interval[1])
                end = max(end, interval[1])
            else:
                intcount += 1
                res.append(interval)
                end = interval[1]

        return res