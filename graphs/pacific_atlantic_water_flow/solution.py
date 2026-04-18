from collections import deque
from typing import List


class Solution:
    """
    Task:
    You are given a rectangular island heights where heights[r][c] represents the height
    above sea level of the cell at coordinate (r, c).

    The islands borders the Pacific Ocean from the top and left sides, and borders the Atlantic Ocean
    from the bottom and right sides.

    Water can flow in four directions (up, down, left, or right) from a cell to a neighboring cell
    with height equal or lower. Water can also flow into the ocean from cells adjacent to the ocean.

    Find all cells where water can flow from that cell to both the Pacific and Atlantic oceans.
    Return it as a 2D list where each element is a list [r, c] representing the row and column of the cell.
    You may return the answer in any order.


    Solution:
    Multi-source BFS starting from the ocean borders and flowing "uphill" to higher elevations. 
    It uses a single queue and a 3D visited array to track both Pacific and Atlantic reachability 
    simultaneously, propagating updated access states to valid neighbors.
    """

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        q = deque()
        res = []
        visited = [[[0, 0] for _ in range(cols)] for _ in range(rows)]
        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for col in range(cols):
            visited[0][col][0] = 1
            q.append((0, col))
            visited[rows - 1][col][1] = 1
            q.append((rows - 1, col))

        for row in range(rows):
            visited[row][0][0] = 1
            if sum(visited[row][0]) == 1:
                q.append((row, 0))
            visited[row][cols - 1][1] = 1
            if sum(visited[row][cols - 1]) == 1:
                q.append((row, cols - 1))

        while q:
            curr_r, curr_c = q.popleft()
            for move in moves:
                move_r = curr_r + move[0]
                move_c = curr_c + move[1]

                if 0 <= move_r < rows and 0 <= move_c < cols:
                    if heights[move_r][move_c] >= heights[curr_r][curr_c]:
                        vis_new_r = max(visited[curr_r][curr_c][0], visited[move_r][move_c][0])
                        vis_new_c = max(visited[curr_r][curr_c][1], visited[move_r][move_c][1])

                        if visited[move_r][move_c][0] != vis_new_r or visited[move_r][move_c][1] != vis_new_c:
                            visited[move_r][move_c] = [vis_new_r, vis_new_c]
                            q.append((move_r, move_c))

        for row in range(rows):
            for col in range(cols):
                if sum(visited[row][col]) == 2:
                    res.append([row, col])

        return res