"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""

from typing import Callable


def isValid(s: str) -> bool:
    opened_parentheses = []
    for char in s:
        if char in ["(", "[", "{"]:
            opened_parentheses.append(char)
        elif char in [")", "]", "}"]:
            if len(opened_parentheses) == 0:
                return False
            last_opened = opened_parentheses.pop()
            if (
                (char == ")" and last_opened != "(")
                or (char == "]" and last_opened != "[")
                or (char == "}" and last_opened != "{")
            ):
                return False
    return len(opened_parentheses) == 0


def test_function(f: Callable) -> None:
    assert f("()") == True
    assert f("()[]{}") == True
    assert f("(]") == False
    assert f("(){}}{") == False


if __name__ == "__main__":
    test_function(isValid)
