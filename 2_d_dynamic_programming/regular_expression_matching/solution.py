class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """
        Task:
        You are given an input string s consisting of lowercase english letters,
        and a pattern p consisting of lowercase english letters, as well as '.', and '*' characters.
        Return true if the pattern matches the entire input string, otherwise return false.
        '.' Matches any single character
        '*' Matches zero or more of the preceding element.


        Solution:
        The dp[i][j] value represents whether the prefix s[0...i-1] matches
        the prefix p[0...j-1].

        Transitions:
        - If p[j-1] is not '*', it matches if the characters match (or p[j-1] == '.')
          and the previous state dp[i-1][j-1] is True.
        - If p[j-1] is '*', it can either represent zero occurrences of the
          preceding character (dp[i][j-2]) or one/more occurrences (dp[i-1][j]),
          provided that the preceding pattern character matches s[i-1] or is '.'.
        """
        n = len(s)
        m = len(p)

        dp = [[False for _ in range(m + 1)] for _ in range(n + 1)]
        dp[0][0] = True

        for j in range(2, m + 1):
            if p[j - 1] == "*" and dp[0][j - 2]:
                dp[0][j] = True

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if p[j - 1] != "*":
                    if p[j - 1] == "." or s[i - 1] == p[j - 1]:
                        dp[i][j] = dp[i - 1][j - 1]
                else:
                    if s[i - 1] == p[j - 2] or p[j - 2] == ".":
                        dp[i][j] = dp[i - 1][j]
                    dp[i][j] = dp[i][j] or dp[i][j - 2]

        return dp[n][m]