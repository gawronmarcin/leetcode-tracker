from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        Task:
        Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of dictionary words.
        You are allowed to reuse words in the dictionary an unlimited number of times. You may assume all dictionary words are unique.


        Solution:
        Bottom-up dynamic programming approach.
        A DP array of size n+1 stores boolean values, where DP[i] indicates whether
        the substring s[0:i] can be segmented into dictionary words. We iterate through
        the string length from left to right. At each step 'i', we look backward by
        checking every word in the dictionary. If the word fits within the current
        bounds (i >= len(word)), the substring immediately preceding this word was
        successfully segmented (DP[i - len(word)] is True), and the extracted text
        exactly matches the dictionary word, it means a valid segmentation exists up
        to index 'i'. We then set DP[i] to True and break the inner loop.
        """
        n = len(s)
        DP = [False for _ in range(n + 1)]
        DP[0] = True

        for i in range(1, n + 1):
            for word in wordDict:
                if i >= len(word):
                    if DP[i - len(word)]:
                        if s[i - len(word):i] == word:
                            DP[i] = True
                            break

        return DP[n]