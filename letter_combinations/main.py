"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.


Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = ""
Output: []
Example 3:

Input: digits = "2"
Output: ["a","b","c"]


Constraints:

0 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].
"""


def letterCombinations(digits):

    if len(digits) < 1:
        return []
    amap = {
        "2": list("abc"),
        "3": list("def"),
        "4": list("ghi"),
        "5": list("jkl"),
        "6": list("mno"),
        "7": list("pqrs"),
        "8": list("tuv"),
        "9": list("wxyz"),
    }
    res = amap[digits[0]]

    for d in digits[1:]:
        print(res)
        _update = []
        for c in amap[d]:
            for r in res:
                _update.append(r + c)

        res = _update

    return res


def test_function(f):
    assert f("2") == ["a", "b", "c"]


test_function(letterCombinations)
