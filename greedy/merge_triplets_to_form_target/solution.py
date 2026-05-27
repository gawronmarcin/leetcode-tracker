from typing import List

class Solution:
    """
    Task:
    You are given a 2D array of integers triplets, where triplets[i] = [ai, bi, ci] represents the ith triplet. You are also given an array of integers target = [x, y, z] which is the triplet we want to obtain.

    To obtain target, you may apply the following operation on triplets zero or more times:

    Choose two different triplets triplets[i] and triplets[j] and update triplets[j] to become [max(ai, aj), max(bi, bj), max(ci, cj)].
    * E.g. if triplets[i] = [1, 3, 1] and triplets[j] = [2, 1, 2], triplets[j] will be updated to [max(1, 2), max(3, 1), max(1, 2)] = [2, 3, 2].

    Return true if it is possible to obtain target as an element of triplets, or false otherwise.

    Solution:
    The algorithm iterates through the list of triplets and ignores any
    triplet that contains a value greater than the corresponding value in the
    target. For the remaining valid triplets, it greedily updates the current
    state by taking the maximum value at each of the three positions. Finally,
    it checks if the accumulated state exactly matches the target.
    """

    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        curr = [0, 0, 0]

        for t in triplets:
            if t[0] <= target[0] and t[1] <= target[1] and t[2] <= target[2]:
                curr[0] = max(curr[0], t[0])
                curr[1] = max(curr[1], t[1])
                curr[2] = max(curr[2], t[2])

        return curr == target