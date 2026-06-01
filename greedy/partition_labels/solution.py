class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        """
        Task:
        You are given a string s consisting of lowercase english letters.

        We want to split the string into as many substrings as possible, while ensuring that each letter appears in at most one substring.

        Return a list of integers representing the size of these substrings in the order they appear in the string.

        Solution:
        The algorithm uses a greedy approach and consists of two phases.
        First, it iterates through the string to record the index of the last
        occurrence of each letter in an array. In the second pass, it iterates
        through the text, continuously updating the furthest reach (max_end)
        for the characters in the currently built partition. When the current
        index matches this maximum reach, it means that none of the letters
        present in the current fragment will appear in the rest of the text.
        The partition is then closed, its size is added to the results,
        and the size counter is reset.
        """
        last_occurrence = [0] * 26

        for i, char in enumerate(s):
            last_occurrence[ord(char) - ord('a')] = i

        res = []
        max_end = 0
        size = 0

        for i, char in enumerate(s):
            max_end = max(max_end, last_occurrence[ord(char) - ord('a')])
            size += 1

            if i == max_end:
                res.append(size)
                size = 0

        return res