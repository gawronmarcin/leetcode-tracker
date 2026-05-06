import pytest
from solution import Solution

def test_countSubstrings_basic_abc():
    sol = Solution()
    assert sol.countSubstrings("abc") == 3

def test_countSubstrings_basic_aaa():
    sol = Solution()
    assert sol.countSubstrings("aaa") == 6

def test_countSubstrings_single_character():
    sol = Solution()
    assert sol.countSubstrings("x") == 1

def test_countSubstrings_even_length_palindrome():
    sol = Solution()
    assert sol.countSubstrings("abba") == 6

def test_countSubstrings_no_multichar_palindromes():
    sol = Solution()
    assert sol.countSubstrings("abcdef") == 6