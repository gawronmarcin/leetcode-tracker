from collections import deque
from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        This solution uses a multi-source Breadth-First Search (BFS) to identify and preserve 
        all 'O' regions connected to the borders of the matrix. It first scans the perimeter 
        and temporarily marks any border 'O' (and its connected 'O' neighbors via BFS) with a 'T'. 
        After all safe regions are marked, a final pass through the matrix converts the 
        remaining surrounded 'O' cells to 'X' and restores the temporarily marked 'T' cells 
        back to 'O'. This approach modifies the board in-place.
        """
        if not board or not board[0]:
            return

        rows = len(board)
        cols = len(board[0])
        q = deque()
        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for col in range(cols):
            if board[0][col] == "O":
                board[0][col] = "T"
                q.append((0, col))
            if board[rows - 1][col] == "O":
                board[rows - 1][col] = "T"
                q.append((rows - 1, col))

        for row in range(1, rows - 1):
            if board[row][0] == "O":
                board[row][0] = "T"
                q.append((row, 0))
            if board[row][cols - 1] == "O":
                board[row][cols - 1] = "T"
                q.append((row, cols - 1))

        while q:
            curr_r, curr_c = q.popleft()
            for move in moves:
                move_r = curr_r + move[0]
                move_c = curr_c + move[1]
                if 0 <= move_r < rows and 0 <= move_c < cols and board[move_r][move_c] == "O":
                    board[move_r][move_c] = "T"
                    q.append((move_r, move_c))

        for row in range(rows):
            for col in range(cols):
                if board[row][col] != "T":
                    board[row][col] = "X"
                else:
                    board[row][col] = "O"