"""
Given the head of a linked list, reverse the nodes of the list k at a time,
and return the modified list. k is a positive integer and is less than or equal to the length
of the linked list. If the number of nodes is not a multiple of k then left-out nodes,
in the end, should remain as it is. You may not alter the values in the list's nodes,
only nodes themselves may be changed.

Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]

Example 2:
Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]

Constraints:
The number of nodes in the list is n.
1 <= k <= n <= 5000
0 <= Node.val <= 1000
"""

from typing import Optional, Callable


class ListNode:  # pylint: disable=too-few-public-methods
    """Definition for singly-linked list."""

    def __init__(self, val=0, next=None):  # pylint: disable=redefined-builtin
        self.val = val
        self.next = next


def reverse_k_group(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    """Reverses the nodes of the list k at a time and returns the modified list"""
    # Check if we need to reverse the group
    current = head
    for _ in range(k):
        if not current:
            return head
        current = current.next

    # Reverse the group (basic way to reverse linked list)
    prev = None
    current = head
    for _ in range(k):
        nxt = current.next
        current.next = prev
        prev = current
        current = nxt

    # After reverse, we know that `head` is the tail of the group.
    # And `curr` is the next pointer in original linked list order
    head.next = reverse_k_group(current, k)
    return prev


def test_function(function: Callable) -> None:
    """Test function for reverseKGroup"""

    def create_linked_list(nums):
        """Creates a linked list from a list of numbers and returns the head."""
        dummy = ListNode(0)
        current = dummy
        for num in nums:
            current.next = ListNode(num)
            current = current.next
        return dummy.next

    def linked_list_to_list(head):
        """Converts a linked list to a list of numbers."""
        result = []
        current = head
        while current:
            result.append(current.val)
            current = current.next
        return result

    # Define test cases: each test case is a tuple (input_list, k, expected_output_list)
    test_cases = [
        # Test case 1: Standard case with k=2
        ([1, 2, 3, 4, 5], 2, [2, 1, 4, 3, 5]),
        # Test case 2: Standard case with k=3
        ([1, 2, 3, 4, 5], 3, [3, 2, 1, 4, 5]),
        # Test case 3: k=1, should return the same list
        ([1, 2, 3], 1, [1, 2, 3]),
        # Test case 4: k larger than the list length
        ([1, 2], 3, [1, 2]),
        # Test case 5: Empty list
        ([], 2, []),
        # Test case 6: k equals the list length
        ([1, 2, 3], 3, [3, 2, 1]),
        # Test case 7: List length is a multiple of k
        ([1, 2, 3, 4, 5, 6], 2, [2, 1, 4, 3, 6, 5]),
        # Test case 8: List length is a multiple of k
        ([1, 2, 3, 4, 5, 6], 3, [3, 2, 1, 6, 5, 4]),
        # Test case 9: Single element list
        ([1], 1, [1]),
    ]

    passed = 0
    total = len(test_cases)

    for idx, (input_list, k, expected_output) in enumerate(test_cases):
        head = create_linked_list(input_list)
        result_head = function(head, k)
        result_list = linked_list_to_list(result_head)
        if result_list == expected_output:
            passed += 1
            print(f"Test case {idx + 1} passed.")
        else:
            print(f"Test case {idx + 1} failed.")
            print(f"Input: {input_list}, k={k}")
            print(f"Expected Output: {expected_output}")
            print(f"Actual Output:   {result_list}")

    print(f"Passed {passed}/{total} test cases.")
