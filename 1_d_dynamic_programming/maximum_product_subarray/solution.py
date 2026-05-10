class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        """
        Task:
        Given an integer array nums, find a subarray that has the largest product within the array and return it.
        A subarray is a contiguous non-empty sequence of elements within an array.
        You can assume the output will fit into a 32-bit integer.

        Dynamic programming algorithm.
        At each step, it tracks the maximum and minimum product of a contiguous
        subarray ending exactly at the current element. Tracking the minimum is
        crucial because a negative number, when multiplied by the current minimum
        (which might also be negative), can yield a new maximum. The global
        result (res) records the highest local maximum observed during the
        entire traversal.
        """
        curr_max = nums[0]
        curr_min = nums[0]
        res = nums[0]

        for num in nums[1:]:
            tmp = curr_max
            curr_max = max(num, tmp * num, curr_min * num)
            curr_min = min(num, tmp * num, curr_min * num)
            res = max(res, curr_max)

        return res