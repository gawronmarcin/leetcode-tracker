import random

"""
Problem:
The Byteland highway is a straight line of length T in Z+ kilometers. 
During winter, over n consecutive days, snow falls on certain segments of the highway. 
On the i-th day, snow falls on the segment [a_i, b_i] (closed on both sides, 
where a_i, b_i in {0, 1, ..., T - 1}). 
As a result of the snowfall, the thickness of the snow layer on this segment 
increases by 1 mm. Where is the most snow?

Algorithm: Sweep-line 
Instead of iterating over every single kilometer (which is too slow for large T),
we only track the exact points where the snow depth changes.
1. For each snowfall [a, b], we add an event at 'a' (+1 snow) and at 'b + 1' (-1 snow).
   The '+1' shift is crucial because the interval is closed, so snow still lies at 'b'.
2. We sort all events from left to right.
3. We sweep through the sorted list, keeping a running sum of the snow thickness.
   Whenever it increases, we check if it's a new record and save the position.
"""


def partition3(T, p, r):
    x = random.randint(p, r)
    pivot = T[x]

    i = p
    lt = p
    gt = r

    while i <= gt:
        if T[i] < pivot:
            T[lt], T[i] = T[i], T[lt]
            lt += 1
            i += 1
        elif T[i] > pivot:
            T[i], T[gt] = T[gt], T[i]
            gt -= 1
        else:
            i += 1

    return lt, gt


def quicksort(T, p, r):
    while p < r:
        lt, gt = partition3(T, p, r)

        if lt - p < r - gt:
            quicksort(T, p, lt - 1)
            p = gt + 1
        else:
            quicksort(T, gt + 1, r)
            r = lt - 1


class Solution:
    def solve(self, n, t_len, intervals):
        events = [0] * (2 * n)

        for i in range(n):
            val1, val2 = intervals[i]

            start_idx = min(val1, val2)
            end_idx = max(val1, val2)

            events[2 * i] = (start_idx, 1)
            events[2 * i + 1] = (end_idx + 1, -1)

        quicksort(events, 0, 2 * n - 1)

        current_sum = 0
        maksi_sum = 0
        maksi_sum_val = 0

        for pos, val in events:
            current_sum += val

            if current_sum > maksi_sum:
                maksi_sum = current_sum
                maksi_sum_val = pos

        return (maksi_sum, maksi_sum_val)