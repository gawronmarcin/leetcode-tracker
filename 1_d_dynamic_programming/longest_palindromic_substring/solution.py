"""
Task:
Given a string s, return the longest substring of s that is a palindrome.
A palindrome is a string that reads the same forward and backward.
If there are multiple palindromic substrings that have the same length, return any one of them.


Solution:
Finds the longest palindromic substring using the Expand Around Center approach.
It iterates through the string, checking for both odd and even length palindromes
by expanding outwards from each possible center.
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        longest = ""

        for i in range(n):
            l, r = i, i
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            if r - l - 1 > len(longest):
                longest = s[l + 1:r]

            l, r = i, i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            if r - l - 1 > len(longest):
                longest = s[l + 1:r]

        return longest