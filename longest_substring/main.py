"""
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

Constraints:
0 <= s.length <= 5 * 10^4
s consists of English letters, digits, symbols and spaces.
"""
def lengthOfLongestSubstring(s: str) -> int:
    char_map = {}
    max_length = 0
    start = 0

    for i, char in enumerate(s):
        if char in char_map and char_map[char] >= start:
            start = char_map[char] + 1
        char_map[char] = i
        max_length = max(max_length, i - start + 1)
    print(max_length)
    return max_length

def test_function(f):
    assert f("abcabcbb") == 3, "Test case 1 failed"
    assert f("bbbbb") == 1, "Test case 2 failed"
    assert f("pwwkew") == 3, "Test case 3 failed"
    assert f("pwke") == 4, "Test case 4 failed"

test_function(lengthOfLongestSubstring)