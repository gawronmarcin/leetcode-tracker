class Solution:
    def checkValidString(self, s: str) -> bool:
        """
        Task:
        You are given a string s which contains only three types of characters: '(', ')' and '*'.

        Return true if s is valid, otherwise return false.

        A string is valid if it follows all of the following rules:

        Every left parenthesis '(' must have a corresponding right parenthesis ')'.
        Every right parenthesis ')' must have a corresponding left parenthesis '('.
        Left parenthesis '(' must go before the corresponding right parenthesis ')'.
        A '*' could be treated as a right parenthesis ')' character or a left parenthesis '(' character, or as an empty string "".


        Solution:
        Greedy algorithm tracking the minimum and maximum possible open parentheses.
        '(' increments both bounds, ')' decrements both, and '*' expands the range.
        If max_open becomes negative, there are too many closing parentheses.
        If min_open becomes negative, we reset it to 0, effectively treating an
        excessive closing attempt via '*' as an empty string instead.
        The string is valid if min_open equals 0 at the end.
        """
        max_open = 0
        min_open = 0

        for char in s:
            if char == "(":
                max_open += 1
                min_open += 1
            elif char == ")":
                max_open -= 1
                min_open -= 1
            else:
                max_open += 1
                min_open -= 1

            if min_open < 0:
                min_open = 0
            if max_open < 0:
                return False

        return min_open == 0