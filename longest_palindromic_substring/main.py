"""
Given a string s, find the longest palindromic substring in s.
Constraints:
1 <= s.length <= 10^5
s consists of only lowercase English letters.

Example 1:
Input: s = "babad"
Output: "bab"

Example 2:
Input: s = "cbbd"
Output: "bb"
"""
def longestPalindrome(s: str) -> str:
    def expandAroundCenter(s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1
    start, end = 0, 0

    for i in range(len(s)):
        len1 = expandAroundCenter(s, i, i)
        len2 = expandAroundCenter(s, i, i + 1)
        max_len = max(len1, len2)

        if max_len > end - start:
            start = i - (max_len - 1) // 2
            end = i + max_len // 2

    return s[start:end + 1]

def test_function(f):
    assert f("babad") == "bab" or f("babad") == "aba", "Test case 1 failed"
    assert f("cbbd") == "bb", "Test case 2 failed"
    assert f("cbbaabd") == "baab", "Test case 3 failed"
    assert f("a") == "a", "Test case 4 failed"
    assert f("ac") == "a" or f("ac") == "c", "Test case 5 failed"

test_function(longestPalindrome)
