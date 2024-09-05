"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:
Input: head = [1], n = 1
Output: []

Example 3:
Input: head = [1,2], n = 1
Output: [1]

Constraints:
The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz

"""

from typing import List


# First solution: Store what we see in list
# Second solution: 2 pointers
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeNthFromEnd(head, n):
    dummy = fast = slow = ListNode(0, next=head)
    for _ in range(n):
        fast = fast.next

    while fast.next:
        fast = fast.next
        slow = slow.next

    slow.next = slow.next.next  # This will ALWAYS exists
    return dummy.next


def list_to_linkedlist(lst: List[int]) -> ListNode:
    dummy = ListNode(0)
    curr = dummy
    for val in lst:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next


def linkedlist_to_list(node: ListNode) -> List[int]:
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result


def test_function(f: callable) -> None:
    assert linkedlist_to_list(f(list_to_linkedlist([1, 2]), 1)) == [1]
    assert linkedlist_to_list(f(list_to_linkedlist([1]), 1)) == []
    assert linkedlist_to_list(f(list_to_linkedlist([1, 2, 3, 4, 5]), 2)) == [1, 2, 3, 5]


test_function(removeNthFromEnd)
