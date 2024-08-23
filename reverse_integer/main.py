"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:
Input: x = 123
Output: 321

Example 2:
Input: x = -123
Output: -321

Example 3:
Input: x = 120
Output: 21

Example 4:
Input: x = -120
Output: -21
"""
def reverse(x):
    def reverse_helper(x, result):
        if x == 0:
            if result < -2 ** 31 or result > 2 ** 31 - 1:
                return 0
            return result
        else:
            return reverse_helper(x // 10, result * 10 + x % 10)

    if x < 0:
        return -reverse(-x)
    else:
        return reverse_helper(x, 0)


def test_function(f):
    assert f(123) == 321, "Test case 1 failed"
    assert f(-123) == -321, "Test case 2 failed"
    assert f(120) == 21, "Test case 3 failed"
    assert f(-120) == -21, "Test case 4 failed"
    assert f(1534236469) == 0, "Test case 5 failed"


test_function(reverse)
