"""
Given a linked list, swap every two adjacent nodes and return its head.
You must solve the problem without modifying the values in the list's nodes
(i.e., only nodes themselves may be changed.)

Example 1:
Input: head = [1,2,3,4]
Output: [2,1,4,3]

Example 2:
Input: head = []
Output: []

Example 3:
Input: head = [1]
Output: [1]

Example 4:
Input: head = [1,2,3]
Output: [2,1,3]

Constraints:
The number of nodes in the list is in the range [0, 100].
0 <= Node.val <= 100
"""

from typing import Optional, Callable


class ListNode:  # pylint:disable=too-few-public-methods
    """Definition for singly-linked list."""

    def __init__(self, val=0, next=None):  # pylint:disable=redefined-builtin
        self.val = val
        self.next = next


def swap_pairs(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Swaps every two adjacent nodes in a linked list and returns the modified list.
    """
    dummy = ListNode(0, head)
    previous, current = dummy, head

    while current and current.next:
        next_pair_node = current.next.next
        second = current.next

        second.next = current
        current.next = next_pair_node
        previous.next = second

        previous = current
        current = next_pair_node

    return dummy.next


def test_function(function: Callable) -> None:
    """Test function for swapPairs"""

    def list_to_linked_list(arr: list) -> Optional[ListNode]:
        """Helper function to convert a list to a linked list"""
        if not arr:
            return None
        head = ListNode(arr[0])
        current = head
        for val in arr[1:]:
            current.next = ListNode(val)
            current = current.next
        return head

    def linked_list_to_list(node: Optional[ListNode]) -> list:
        """Helper function to convert a linked list to a list"""
        result = []
        while node:
            result.append(node.val)
            node = node.next
        return result

    # Test case 1: Swap pairs in a linked list with even number of elements
    head = list_to_linked_list([1, 2, 3, 4])
    result = function(head)
    assert linked_list_to_list(result) == [
        2,
        1,
        4,
        3,
    ], f"Failed test case 1: {linked_list_to_list(result)}"

    # Test case 2: Swap pairs in a linked list with an odd number of elements
    head = list_to_linked_list([1, 2, 3, 4, 5])
    result = function(head)
    assert linked_list_to_list(result) == [
        2,
        1,
        4,
        3,
        5,
    ], f"Failed test case 2: {linked_list_to_list(result)}"

    # Test case 3: Empty linked list
    head = list_to_linked_list([])
    result = function(head)
    assert not linked_list_to_list(result), f"Failed test case 3: {linked_list_to_list(result)}"

    # Test case 4: Linked list with one element
    head = list_to_linked_list([1])
    result = function(head)
    assert linked_list_to_list(result) == [1], f"Failed test case 4: {linked_list_to_list(result)}"

    print("All test cases passed!")


test_function(swap_pairs)
