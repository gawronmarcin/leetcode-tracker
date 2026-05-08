"""
Task:
A string consisting of uppercase english characters can be encoded to a number using the following mapping:

'A' -> "1"
'B' -> "2"
...
'Z' -> "26"
To decode a message, digits must be grouped and then mapped back into letters using the reverse of the mapping above. There may be multiple ways to decode a message. For example, "1012" can be mapped into:

"JAB" with the grouping (10 1 2)
"JL" with the grouping (10 12)
The grouping (1 01 2) is invalid because 01 cannot be mapped into a letter since it contains a leading zero.

Given a string s containing only digits, return the number of ways to decode it. You can assume that the answer fits in a 32-bit integer.


Solution:
Dynamic Programming: Iteratively builds the number of valid decoding ways up to index i by evaluating single and double-digit combinations.
"""
class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        F = [0] * n

        if s[0] == "0":
            return 0
        else:
            F[0] = 1

        for i in range(1, n):
            if s[i] != "0":
                F[i] += F[i - 1]

            if 10 <= int(s[i - 1] + s[i]) <= 26:
                if i >= 2:
                    F[i] += F[i - 2]
                else:
                    F[i] += 1

        return F[n - 1]