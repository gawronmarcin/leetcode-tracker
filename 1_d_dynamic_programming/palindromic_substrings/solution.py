class Solution:
    def countSubstrings(self, s: str) -> int:
        """
        Task:
        Given a string s, return the number of substrings within s that are palindromes.
        A palindrome is a string that reads the same forward and backward.


        Solution:
        Calculates the number of palindromic substrings using Dynamic Programming.
        A 2D array is used to keep track of whether a substring from index i to j is a palindrome.
        Note: This is not the most space-optimal solution (O(N^2) memory complexity),
        but it was written specifically to practice the Dynamic Programming approach.
        """
        n = len(s)
        is_palindrome = [[0] * n for _ in range(n)]
        res = 0

        for i in range(n):
            is_palindrome[i][i] = 1
            res += 1

        for i in range(n - 1):
            if s[i] == s[i + 1]:
                is_palindrome[i][i + 1] = 1
                res += 1

        for l in range(3, n + 1):
            i = 0
            while i + l - 1 < n:
                if s[i] == s[i + l - 1] and is_palindrome[i + 1][i + l - 2]:
                    is_palindrome[i][i + l - 1] = 1
                    res += 1
                i += 1

        return res