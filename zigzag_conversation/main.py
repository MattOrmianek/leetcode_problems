"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

Example:

P   A   H   N
A P L S I I G
Y   I   E   .

And then read line by line: "PAHNAPLSIIGYEI"

Write the code that will take a string and make this conversation between the person reading the message and the person giving the message.

Example:

Input: "PAYPALISHIRING"
Output: "PAHNAPLSIIGYEI"
"""
def zigzag_conversation(s: str, rows: int) -> str:
    list_of_string = list(s)
    skip = False
    for i in range(len(list_of_string)):
        if skip:
            skip = False
            print("skipped")
            continue
        element = list_of_string[i]
        print(element)


        index = i + 1
        if index % rows == 0:
            print()
            print(list_of_string[i+1])
            print()
            skip = True


def test_function(f):
    assert f("PAYPALISHIRING", 3) == "PAHNAPLSIIGYEI", "Test case 1 failed"

test_function(zigzag_conversation)