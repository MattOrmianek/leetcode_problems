"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

Example 2:
Input: (5 -> 6) + (5 -> 6)
Output: 0 -> 0
Explanation: 56 + 56 = 112.
"""

def add_two_numbers(l1: list, l2: list) -> list:
    """
    Add two number to each other
    """
    output = []
    carry = 0
    for i in range(len(l1)):

        if i < len(l1):
            value1 = l1[i]
        else:
             value2 = 0

        if i < len(l2):
             value2 = l2[i]
        else:
             value2 = 0
        calculated = value1 + value2 + carry
        if carry != 0:
            carry = 0
        if calculated > 9:
                calculated = 0
                carry = 1
        output.append(calculated)
    print(output[::-1])

l1 = [5,6]
l2 = [5,6]
add_two_numbers(l1,l2)
l1 = [2,4,3]
l2 = [5,6,4]
add_two_numbers(l1,l2)
l1 = [9,9,9,9,9,9,9]
l2 = [9,9,9,9]
add_two_numbers(l1,l2) #Output: [8,9,9,9,0,0,0,1]
