import pytest
from solution import Solution

def test_standard_path():
    sol = Solution()
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    assert sol.ladderLength(beginWord, endWord, wordList) == 5

def test_end_word_missing():
    sol = Solution()
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log"]
    assert sol.ladderLength(beginWord, endWord, wordList) == 0

def test_no_possible_path():
    sol = Solution()
    beginWord = "hot"
    endWord = "dog"
    wordList = ["hot", "dog"]
    assert sol.ladderLength(beginWord, endWord, wordList) == 0

def test_direct_connection():
    sol = Solution()
    beginWord = "hit"
    endWord = "hot"
    wordList = ["hot", "dot", "dog"]
    assert sol.ladderLength(beginWord, endWord, wordList) == 2

def test_begin_word_in_list():
    sol = Solution()
    beginWord = "a"
    endWord = "c"
    wordList = ["a", "b", "c"]
    assert sol.ladderLength(beginWord, endWord, wordList) == 2