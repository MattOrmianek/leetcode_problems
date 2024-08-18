## Explanation of lengthOfLongestSubstring Function
The lengthOfLongestSubstring function is designed to find the length of the longest substring without repeating characters in a given string s. The function uses a sliding window technique combined with a hash map to efficiently determine the length of the longest such substring.

## Function Explanation

```python
def lengthOfLongestSubstring(s: str) -> int:
    char_map = {}
    max_length = 0
    start = 0

    for i, char in enumerate(s):
        if char in char_map and char_map[char] >= start:
            start = char_map[char] + 1
        char_map[char] = i
        max_length = max(max_length, i - start + 1)

    return max_length
```
Key Components: <br>
## char_map:

A dictionary (char_map) is used to store the last seen index of each character in the string s.
The keys in char_map represent characters in the string, and the values represent their most recent positions (indices).
## max_length:

This variable keeps track of the length of the longest substring without repeating characters found so far.
## start:

This variable marks the start index of the current substring being considered. If a repeating character is found within the current substring, start is updated to the index right after the last occurrence of that character.
## Main Loop (for i, char in enumerate(s)):

The loop iterates through each character in the string s, with i representing the current index and char representing the current character.
##Checking for Repeating Characters:
If char is already in char_map and its last seen index is greater than or equal to start, it indicates that the character has been encountered within the current substring.
In this case, start is updated to char_map[char] + 1, effectively moving the start of the current substring to just after the last occurrence of the repeating character.
## Updating char_map:
The current character's index is stored in char_map.
## Updating max_length:
The length of the current substring (i - start + 1) is calculated and compared with max_length. If it's greater, max_length is updated.
## Example Walkthrough


Input:
```python
s = "pwke"
```
Step-by-Step Execution: <br>
Initialization:
```python
char_map = {}
max_length = 0
start = 0
```
Iteration:

Index 0: 'p' <br>

'p' is not in char_map.<br>
Update char_map: {'p': 0}<br>
Update max_length: max_length = max(0, 0 - 0 + 1) = 1<br>
Index 1: 'w'<br>

'w' is not in char_map.<br>
Update char_map: {'p': 0, 'w': 1}<br>
Update max_length: max_length = max(1, 1 - 0 + 1) = 2<br>
Index 2: 'k'<br>

'k' is not in char_map.<br>
Update char_map: {'p': 0, 'w': 1, 'k': 2}<br>
Update max_length: max_length = max(2, 2 - 0 + 1) = 3<br>
Index 3: 'e'<br>

'e' is not in char_map.<br>
Update char_map: {'p': 0, 'w': 1, 'k': 2, 'e': 3}<br>
Update max_length: max_length = max(3, 3 - 0 + 1) = 4<br>
## Final Result:<br>

The longest substring without repeating characters in "pwke" is "pwke".
The function returns 4 as the length of this substring.
## Conclusion
The lengthOfLongestSubstring function efficiently calculates the length of the longest substring without repeating characters in a string by using a sliding window approach and a hash map. The time complexity of this solution is O(n), where n is the length of the string, making it highly efficient for large inputs.