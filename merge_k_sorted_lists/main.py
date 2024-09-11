"""
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
Merge all the linked-lists into one sorted linked-list and return it.

Example 1:
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[1->4->5,
1->3->4,
2->6]
merging them into one sorted list:
1->1->2->3->4->4->5->6

Example 2:
Input: lists = []
Output: []

Example 3:
Input: lists = [[]]
Output: []

Constraints:
k == lists.length
0 <= k <= 104
0 <= lists[i].length <= 500
-104 <= lists[i][j] <= 104
lists[i] is sorted in ascending order.
The sum of lists[i].length will not exceed 104.
"""

import heapq
from typing import List, Optional, Callable


class ListNode:  # pylint: disable=too-few-public-methods
    """Definition for singly-linked list."""

    def __init__(self, val=0, next=None) -> None:  # pylint: disable=redefined-builtin
        self.val = val
        self.next = next


def merge_k_lists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    """This is merging k lists together"""
    priority_queue = []

    for index, value in enumerate(lists):
        if value:
            heapq.heappush(priority_queue, (value.val, index, value))

    dummy = ListNode()
    curr = dummy
    while priority_queue:
        value, index, node = heapq.heappop(priority_queue)
        curr.next = node
        curr = curr.next

        if node.next:
            heapq.heappush(priority_queue, (node.next.val, index, node.next))

    return dummy.next


def test_function(function: Callable) -> None:
    """This is a test function to test the function with different inputs"""

    def create_linked_list(arr: List[int]) -> Optional[ListNode]:
        """Helper function to create a linked list from a list"""
        dummy = ListNode()
        curr = dummy
        for num in arr:
            curr.next = ListNode(num)
            curr = curr.next
        return dummy.next

    def linked_list_to_list(node: Optional[ListNode]) -> List[int]:
        """Helper function to convert a linked list to a list for easier comparison"""
        result = []
        while node:
            result.append(node.val)
            node = node.next
        return result

    # Test case 1: Three lists, simple case
    lists = [
        create_linked_list([1, 4, 5]),
        create_linked_list([1, 3, 4]),
        create_linked_list([2, 6]),
    ]
    result = function(lists)
    assert linked_list_to_list(result) == [1, 1, 2, 3, 4, 4, 5, 6], "Test case 1 failed"

    # Test case 2: One empty list and two non-empty lists
    lists = [create_linked_list([]), create_linked_list([1, 3, 4]), create_linked_list([2, 6])]
    result = function(lists)
    assert linked_list_to_list(result) == [1, 2, 3, 4, 6], "Test case 2 failed"

    # Test case 3: All empty lists
    lists = [create_linked_list([]), create_linked_list([]), create_linked_list([])]
    result = function(lists)
    assert not linked_list_to_list(result), "Test case 3 failed"

    # Test case 4: Single non-empty list
    lists = [create_linked_list([1, 2, 3])]
    result = function(lists)
    assert linked_list_to_list(result) == [1, 2, 3], "Test case 4 failed"

    print("All test cases passed!")


test_function(merge_k_lists)
