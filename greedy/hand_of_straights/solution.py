from queue import PriorityQueue
from typing import List


class Solution:
    """
    Task:
    You are given an integer array hand where hand[i] is the value written on the ith card and an integer groupSize.

    You want to rearrange the cards into groups so that each group is of size groupSize, and card values are consecutively increasing by 1.

    Return true if it's possible to rearrange the cards in this way, otherwise, return false.

    Solution:
    This solution uses a greedy approach combined with a frequency array and a Priority Queue.

    Algorithm steps:
    1. Quick check: If the total number of cards is not divisible by the group size, return False.
    2. Find the maximum card value and create a frequency array `count` to store occurrences.
    3. Push all cards into a Priority Queue to efficiently access the smallest available card.
    4. Iteratively pop the smallest card. If it was already used in a previous group 
       (its count is 0), simply ignore it.
    5. Attempt to build a consecutive sequence of length `groupSize` starting from this smallest 
       card. If the required sequence exceeds the maximum available card value, or if any required 
       consecutive card is missing (count < 1), return False.
    6. Decrease the counts of the used cards and repeat until all cards are successfully grouped.
    """

    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if n % groupSize != 0:
            return False

        m = max(hand)
        count = [0] * (m + 1)

        for num in hand:
            count[num] += 1

        pq = PriorityQueue()
        for num in hand:
            pq.put(num)

        while not pq.empty():
            curr = pq.get()

            if count[curr] == 0:
                continue

            if curr + groupSize - 1 > m:
                return False

            for i in range(groupSize):
                if count[curr + i] < 1:
                    return False
                count[curr + i] -= 1

        return True