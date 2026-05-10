import pytest
from solution import Solution


def test_solve():
    sol = Solution()


    assert sol.wordBreak("neetcode", ["neet", "code"]) == True

    assert sol.wordBreak("applepenapple", ["apple", "pen", "ape"]) == True

    assert sol.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]) == False

    assert sol.wordBreak("programowanie", ["programowanie", "program"]) == True

    assert sol.wordBreak("python", ["java", "c++", "ruby"]) == False