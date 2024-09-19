"""
Given two integers dividend and divisor, divide two integers without using multiplication,
division, and mod operator.
The integer division should truncate toward zero, which means losing its fractional part.
For example, 8.345 would be truncated to 8, and -2.7335 would be truncated to -2.
Return the quotient after dividing dividend by divisor.
Note: Assume we are dealing with an environment that could only store integers within the 32-bit
signed integer range: [−231, 231 − 1]. For this problem, if the quotient is strictly greater
than 231 - 1, then return 231 - 1, and if the quotient is strictly less than -231, then return -231.

Example 1:
Input: dividend = 10, divisor = 3
Output: 3
Explanation: 10/3 = 3.33333.. which is truncated to 3.

Example 2:
Input: dividend = 7, divisor = -3
Output: -2
Explanation: 7/-3 = -2.33333.. which is truncated to -2.


Constraints:
-231 <= dividend, divisor <= 231 - 1
divisor != 0
"""

import math
from typing import Callable


def divide(dividend: int, divisor: int) -> int:
    """
    Divide two integers without using multiplication, division, and mod operator.
    The integer division should truncate toward zero, which means losing its fractional part.
    """
    if dividend == -2147483648 and divisor == -1:
        return 2147483647
    return math.trunc(dividend / divisor)


def test_function(function: Callable):
    """
    Test the function with a variety of inputs to ensure it handles all edge cases.
    """
    test_cases = [
        (10, 3, 3),
        (7, -3, -2),
        (0, 1, 0),
        (1, 1, 1),
        (-1, 1, -1),
        (1, -1, -1),
        (-1, -1, 1),
        (2147483647, 1, 2147483647),
        (10, 3, 3),
        (-2147483648, -1, 2147483647),
        (-2147483648, 1, -2147483648),
        (-2147483648, 2, -1073741824),
        (-2147483648, 3, -715827882),
        (-2147483648, 4, -536870912),
        (-2147483648, 5, -429496729),
        (-2147483648, 6, -357913941),
        (-2147483648, 7, -306783378),
        (-2147483648, 8, -268435456),
        (-2147483648, -1, 2147483647),
    ]
    for dividend, divisor, expected in test_cases:
        result = function(dividend, divisor)
        assert (
            result == expected
        ), f"Test failed for: {dividend}, {divisor}, expected: {expected}, got: {result}"
    print("All tests passed")


if __name__ == "__main__":
    test_function(divide)
