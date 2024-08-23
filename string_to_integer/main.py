"""
Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer.

The algorithm for myAtoi(string s) is as follows:

Whitespace: Ignore any leading whitespace (" ").
Signedness: Determine the sign by checking if the next character is '-' or '+', assuming positivity is neither present.
Conversion: Read the integer by skipping leading zeros until a non-digit character is encountered or the end of the string is reached. If no digits were read, then the result is 0.
Rounding: If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then round the integer to remain in the range. Specifically, integers less than -231 should be rounded to -231, and integers greater than 231 - 1 should be rounded to 231 - 1.
Return the integer as the final result.

Example 1:
Input: "42"
Output: 42

Example 2:
Input: "   -42"
Output: -42

Example 3:
Input: "4193 with words"
Output: 4193

Example 4:
Input: "words and 987"
Output: 0

"""
def myAtoi(s: str) -> int:
    s = s.strip()

    if not s:
        return 0

    sign = 1
    start_index = 0

    if s[0] == '-':
        sign = -1
        start_index = 1
    elif s[0] == '+':
        start_index = 1

    result = 0
    for i in range(start_index, len(s)):
        if s[i].isdigit():
            result = result * 10 + int(s[i])
        else:
            break

    result *= sign

    int_max = 2 ** 31 - 1
    int_min = -2 ** 31
    if result > int_max:
        return int_max
    if result < int_min:
        return int_min

    return result

def test_function(f):
    assert f("42") == 42, "Test case 1 failed"
    assert f("   -42") == -42, "Test case 2 failed"
    assert f("4193 with words") == 4193, "Test case 3 failed"
    assert f("words and 987") == 0, "Test case 4 failed"
    assert f("2147483648") == 2147483647, "Test case 5 failed"
    assert f("-91283472332") == -2147483648, "Test case 6 failed"
    assert f("     +004500") == 4500, "Test case 7 failed"
    assert f("   +0 123") == 0, "Test case 8 failed"
    assert f("    -88827   5655  U") == -88827, "Test case 9 failed"


test_function(myAtoi)