"""
Given two strings needle and haystack, return the index of the first occurrence of needle
in haystack, or -1 if needle is not part of haystack.

Example 1:
Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.

Example 2:
Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.

Constraints:
1 <= haystack.length, needle.length <= 104
haystack and needle consist of only lowercase English letters.
"""

from typing import Callable


def find_needle_in_haystack(haystack: str, needle: str) -> int:
    """
    Find the index of the first occurrence of needle in haystack.
    """
    if needle in haystack:
        return haystack.index(needle)
    return -1


def test_find_needle_in_haystack(func: Callable[[str, str], int]) -> None:
    """
    Test the find_needle_in_haystack function with various test cases.
    """
    test_cases = [
        ("sadbutsad", "sad", 0),
        ("leetcode", "leeto", -1),
    ]
    for haystack, needle, expected in test_cases:
        assert (
            func(haystack, needle) == expected
        ), f"Test case failed: {haystack}, {needle}, {expected}"

    print("All test cases passed!")


if __name__ == "__main__":
    test_find_needle_in_haystack(find_needle_in_haystack)
