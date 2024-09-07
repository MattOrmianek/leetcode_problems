"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]

Constraints:
The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
"""
from typing import Callable
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_two_sorted_lists(list1: ListNode, list2: ListNode) -> ListNode:
    dummy = ListNode()
    current = dummy


    while list1 and list2:
        if list1.val <= list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next

    current.next = list1 if list1 else list2

    return dummy.next


def test_function(f: Callable) -> None:
    def to_linked_list(lst):
        dummy = ListNode()
        current = dummy
        for val in lst:
            current.next = ListNode(val)
            current = current.next
        return dummy.next

    def to_list(node):
        result = []
        while node:
            result.append(node.val)
            node = node.next
        return result

    l1 = to_linked_list([1, 2, 4])
    l2 = to_linked_list([1, 3, 4])
    merged_list = f(l1, l2)
    assert to_list(merged_list) == [1, 1, 2, 3, 4, 4], "Test Case 1 Failed"

    l1 = to_linked_list([])
    l2 = to_linked_list([])
    merged_list = f(l1, l2)
    assert to_list(merged_list) == [], "Test Case 2 Failed"

    l1 = to_linked_list([5, 6, 7])
    l2 = to_linked_list([])
    merged_list = f(l1, l2)
    assert to_list(merged_list) == [5, 6, 7], "Test Case 3 Failed"

    l1 = to_linked_list([1, 3])
    l2 = to_linked_list([2, 4])
    merged_list = f(l1, l2)
    assert to_list(merged_list) == [1, 2, 3, 4], "Test Case 4 Failed"

    print("All test cases passed!")

test_function(merge_two_sorted_lists)