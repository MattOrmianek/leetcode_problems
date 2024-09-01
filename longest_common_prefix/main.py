"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".



Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.


Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.
"""

def longestCommonPrefix(strings):
    """
    :type strs: List[str]
    :rtype: str
    """
    min_len = len(min(strings, key=len))
    common = ""
    for i in range(0, min_len):
        candidate = []
        for string in strings:
            candidate.append(string[i])
        if len(set(candidate)) == 1:
            common += candidate[0]
        else:
            break

    return common


def test_function(f):
    assert f(["flower","flow","flight"]) == "fl"
    assert f(["dog","racecar","car"]) == ""
    assert f(["cir","car"]) == "c"

test_function(longestCommonPrefix)