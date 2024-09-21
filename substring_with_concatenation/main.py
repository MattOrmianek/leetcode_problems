"""
You are given a string s and an array of strings words. All the strings of words are of the same
length.

A concatenated string is a string that exactly contains all the strings of any permutation of words
concatenated.

For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef", "cdefab",
"efabcd", and "efcdab" are all concatenated strings. "acdbef" is not a concatenated string
because it is not the concatenation of any permutation of words.
Return an array of the starting indices of all the concatenated substrings in s. You can
return the answer in any order.
Example 1:
Input: s = "barfoothefoobarman", words = ["foo","bar"]
Output: [0,9]
Explanation:

The substring starting at 0 is "barfoo". It is the concatenation of ["bar","foo"] which is a
permutation of words.
The substring starting at 9 is "foobar". It is the concatenation of ["foo","bar"] which is a
permutation of words.

Example 2:
Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
Output: []
Explanation:
There is no concatenated substring.

Example 3:
Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
Output: [6,9,12]
Explanation:
The substring starting at 6 is "foobarthe". It is the concatenation of ["foo","bar","the"].
The substring starting at 9 is "barthefoo". It is the concatenation of ["bar","the","foo"].
The substring starting at 12 is "thefoobar". It is the concatenation of ["the","foo","bar"].

Constraints:
1 <= s.length <= 10^4
1 <= words.length <= 5000
1 <= words[i].length <= 30
s and words[i] consist of lowercase English letters.
"""

from collections import Counter
from typing import Callable


def find_substring(input_string: str, words: list[str]) -> list[int]:
    """
    Find all the starting indices of all the concatenated substrings in s.
    Each concatenated substring is a combination of all words in 'words' array
    in any order without any intervening characters.
    """
    if not input_string or not words:
        return []

    word_length = len(words[0])
    word_count = len(words)
    words_counter = Counter(words)
    result = []

    for i in range(word_length):
        left = i
        right = i
        seen = {}
        current_count = 0

        while right + word_length <= len(input_string):
            word = input_string[right : right + word_length]
            right += word_length
            if word in words_counter:
                seen[word] = seen.get(word, 0) + 1
                current_count += 1

                # If a word is seen more times than it exists in words_counter,
                # move the left pointer to reduce the count.
                while seen[word] > words_counter[word]:
                    left_word = input_string[left : left + word_length]
                    seen[left_word] -= 1
                    current_count -= 1
                    left += word_length

                # When all words are matched, record the starting index.
                if current_count == word_count:
                    result.append(left)
            else:
                # Reset the window if the word is not in words_counter.
                seen.clear()
                current_count = 0
                left = right

    return result


def test_function(function: Callable):
    """
    Test the function with a variety of inputs to ensure it handles all edge cases.
    """
    test_cases = [
        ("barfoothefoobarman", ["foo", "bar"], [0, 9]),
        ("wordgoodgoodgoodbestword", ["word", "good", "best", "word"], []),
        ("barfoofoobarthefoobarman", ["bar", "foo", "the"], [6, 9, 12]),
        ("", ["foo", "bar"], []),  # Edge case: empty string s
        ("foobar", [], []),  # Edge case: empty words list
        ("foobarfoobar", ["foo", "bar"], [0, 3, 6]),
        ("barfoofoobarthefoobarmanfoo", ["bar", "foo", "the"], [6, 9, 12]),
        ("foobarthefoobarman", ["foo", "bar", "the"], [0, 3, 6]),
        ("barfoofoobarthefoobarmanbarfoo", ["bar", "foo", "the"], [6, 9, 12]),
        ("thefoobarbarfoo", ["foo", "bar", "the"], [0]),
    ]

    for idx, (input_string, words, expected) in enumerate(test_cases, 1):
        result = function(input_string, words)
        assert sorted(result) == sorted(expected), (
            f"Test case {idx} failed:\n"
            f"Input s='{input_string}', words={words}\n"
            f"Expected {expected}, but got {result}"
        )
        print(f"Test case {idx} passed!")

    print("All tests passed!")


if __name__ == "__main__":
    test_function(find_substring)
