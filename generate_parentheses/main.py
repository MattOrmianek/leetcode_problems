"""
Given n pairs of parentheses, write a function to generate all combinations
 of well-formed parentheses.

Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:
Input: n = 1
Output: ["()"]

Constraints:
1 <= n <= 8
"""

from typing import Callable, List


def generate_parenthesis(n: int) -> List[str]:
    """Generate perenthesis function for leetcode problem"""

    def backtrack(current: str = "", left: int = 0, right: int = 0):
        """
        This is a recursive function that builds the parentheses combinations step by step.
        """
        if len(current) == 2 * n:
            # Valid sequence of n pairs of parentheses has been formed
            result.append(current)
            return
        if left < n:
            # Add left parenthesis
            backtrack(current + "(", left + 1, right)
        if right < left:
            # Add right parenthesis
            backtrack(current + ")", left, right + 1)

    result: List[str] = []
    backtrack()
    return result


def test_function(function: Callable):
    """Test function for leetcode problem"""
    assert function(3) == ["((()))", "(()())", "(())()", "()(())", "()()()"], print(function(3))
    assert function(1) == ["()"]
    print("All tests passed")


test_function(generate_parenthesis)
