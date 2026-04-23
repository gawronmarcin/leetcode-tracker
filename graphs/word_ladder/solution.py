"""
Task:
You are given two words, beginWord and endWord, and also a list of words wordList.
All of the given words are of the same length, consisting of lowercase English letters, and are all distinct.
Your goal is to transform beginWord into endWord by following the rules:
You may transform beginWord to any word within wordList, provided that at exactly one position the words have a different character,
and the rest of the positions have the same characters.
You may repeat the previous step with the new word that you obtain, and you may do this as many times as needed.
Return the minimum number of words within the transformation sequence needed to obtain the endWord, or 0 if no such sequence exists.

Solution:
Consists of finding the shortest transformation sequence from a begin word to an end word.
The algorithm uses Breadth-First Search (BFS) to guarantee finding the shortest path in an implicit graph.
I try to avoid using hash-based structures (set/dict), so edges are discovered 'on the fly' by generating
all single-letter mutations of the current word. Their presence in the dictionary is verified 
using an optimized binary search on a pre-sorted list of allowed words.
"""
from collections import deque
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        alphabet = 'abcdefghijklmnopqrstuvwxyz'

        if beginWord not in wordList:
            wordList.append(beginWord)

        wordList.sort()
        n = len(wordList)
        visited = [0] * n

        def binary_search(word: str, word_list: List[str]) -> int:
            p = 0
            r = n - 1
            while p <= r:
                mid = (p + r) // 2
                if word_list[mid] == word:
                    return mid
                if word_list[mid] > word:
                    r = mid - 1
                else:
                    p = mid + 1
            return -1

        start_idx = binary_search(beginWord, wordList)
        visited[start_idx] = 1

        q = deque()
        q.append((beginWord, 1))

        while q:
            word, step = q.popleft()

            for i in range(len(word)):
                letter = word[i]
                for new_char in alphabet:
                    if letter != new_char:
                        new_word = word[:i] + new_char + word[i + 1:]
                        found_idx = binary_search(new_word, wordList)

                        if found_idx > -1:
                            if new_word == endWord:
                                return step + 1
                            if visited[found_idx] == 0:
                                visited[found_idx] = 1
                                q.append((new_word, step + 1))

        return 0