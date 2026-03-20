import random
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        Approach: QuickSelect
        ----------------------------
        This solution uses a partition strategy similar to QuickSort.
        By repeatedly picking a random pivot and discarding the half of 
        the array that does not contain the target, we avoid sorting the 
        entire array, achieving an average time complexity of O(N).
        """

        def partition(T, left, right):
            rand_idx = random.randint(left, right)
            T[rand_idx], T[right] = T[right], T[rand_idx]

            pivot = T[right]
            i = left

            for j in range(left, right):
                if T[j] >= pivot:
                    T[i], T[j] = T[j], T[i]
                    i += 1

            T[i], T[right] = T[right], T[i]

            return i

        left = 0
        right = len(nums) - 1
        target = k - 1

        while left <= right:
            if left == right:
                return nums[left]

            q = partition(nums, left, right)

            if q == target:
                return nums[q]
            elif q < target:
                left = q + 1
            else:
                right = q - 1