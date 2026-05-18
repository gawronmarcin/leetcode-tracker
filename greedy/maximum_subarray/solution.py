"""
Task:
Given an array of integers nums, find the subarray with the largest sum and return the sum.
A subarray is a contiguous non-empty sequence of elements within an array.


Kadane's Algorithm:
This algorithm finds the maximum contiguous subarray sum in O(N) time and O(1) space.
It maintains a running sum (`curr_sum`) of the current subarray.
At each step, if the running sum drops below zero, it is discarded, and a new 
subarray is started from the current element (because a negative prefix would 
only decrease the total sum of any subsequent subarray). Otherwise, the current 
element is added to the running sum. The global maximum sum (`max_sum`) is 
updated continuously to keep track of the highest sum encountered so far.
"""
from math import inf
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum = 0
        max_sum = -inf

        for num in nums:
            if curr_sum < 0:
                curr_sum = num
            else:
                curr_sum += num

            max_sum = max(max_sum, curr_sum)

        return max_sum