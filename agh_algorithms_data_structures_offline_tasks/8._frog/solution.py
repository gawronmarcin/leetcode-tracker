"""
Task:
Algosia has turned into a frog (Żabosia) and is jumping across leaves (and only leaves)
located on a number line. She starts from the leaf at coordinate 0, and her goal is to
reach the leaf at coordinate P. Each leaf has a non-negative integer written on it,
representing the amount of energy points Żabosia gains by jumping onto that leaf.

Determine the minimum number of jumps Żabosia must make to reach the leaf at coordinate P,
given that the cost of a jump of length d is described by the function f(d) = A*d^2 + B*d + C.

Solution:
This algorithm solves the minimum jumps problem using Dynamic Programming.
The current time complexity is O(N^3) and space complexity is O(N^2).
It evaluates the maximum energy retained for each jump configuration.
While it could be optimized to O(N^2) time complexity using the Convex Hull Trick (CHT)
due to the quadratic cost function, it was left as O(N^3) to keep the code simple
and avoid overcomplication.
"""
from math import inf


class Solution:
    def solve(self, P, n, A, B, C, leaves):
        # Filtrowanie śmieciowych liści i dodanie mety
        leaves = [leaf for leaf in leaves if 0 <= leaf[0] < P]
        leaves.sort()
        leaves.append((P, 0))

        # Faktyczna liczba węzłów po filtracji, która chroni przed IndexError
        m = len(leaves) - 1

        dp = [[-inf for _ in range(m + 1)] for _ in range(m + 1)]
        dp[0][0] = leaves[0][1]

        for i in range(1, m + 1):
            for j in range(1, m + 1):
                maksi = -inf

                for k in range(i):
                    dist = leaves[i][0] - leaves[k][0]
                    dif = A * dist * dist + B * dist + C

                    if dp[k][j - 1] - dif >= 0:
                        maksi = max(maksi, dp[k][j - 1] - dif + leaves[i][1])

                dp[i][j] = maksi

                if i == m and dp[i][j] != -inf:
                    return j

        return -1