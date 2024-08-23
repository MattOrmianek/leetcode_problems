"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

Example:

P   A   H   N
A P L S I I G
Y   I   I   .

And then read line by line: "PAHNAPLSIIGYEI"

Write the code that will take a string and make this conversation between the person reading the message and the person giving the message.

Example:

Input: "PAYPALISHIRING"
Output: "PAHNAPLSIIGYEI"
"""
def zigzag_conversation(s: str, rows: int) -> str:
    if len(s) == 0:
        return ""
    if rows == 1:
        return s
    output_str = ""
    for i in range(rows):
        inc = 2 * (rows - 1)
        for j in range(i, len(s), inc):
            output_str += s[j]
            if i > 0 and i < rows - 1 and j + inc - 2 * i < len(s):
                output_str += s[j + inc - 2 * i]
    return output_str




def test_function(f):
    assert f("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR", "Test case 1 failed"
    assert f("PAYPALISHIRING", 4) == "PINALSIGYAHRPI", "Test case 2 failed"
    assert f("A", 1) == "A", "Test case 3 failed"

test_function(zigzag_conversation)