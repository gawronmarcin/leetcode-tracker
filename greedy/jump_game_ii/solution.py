from typing import List
class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        Task:
        You are given an array of integers nums, where nums[i] represents the maximum length of a jump towards the right from index i.
         For example, if you are at nums[i], you can jump to any index i + j where:

        This algorithm uses a greedy approach to find the minimum number of jumps.
        It iterates through the array while maintaining two boundaries: 'max_dist',
        which tracks the farthest index reachable from any examined position, and 
        'curr_window', which marks the end of the current jump's range. When the 
        iteration reaches 'curr_window', it means a jump must be made, the step 
        counter is incremented, and the window is updated to 'max_dist'. The loop
        terminates early if 'curr_window' reaches or exceeds the final index.
        """
        n = len(nums)
        if n <= 1:
            return 0

        steps = 0
        max_dist = 0
        curr_window = 0

        for i in range(n):
            max_dist = max(max_dist, i + nums[i])

            if i == curr_window:
                steps += 1
                curr_window = max_dist

                if curr_window >= n - 1:
                    return steps