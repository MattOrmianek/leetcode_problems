"""
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place.
The order of the elements may be changed. Then return the number of elements in nums
which are not equal to val.
Consider the number of elements in nums which are not equal to val be k, to get accepted,
you need to do the following things:
- Change the array nums such that the first k elements of nums contain the elements which
    are not equal to val. The remaining elements of nums are not important as well as the
    size of nums.
- Return k.

Example 1:
Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).

Example 2:
Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,_,_,_]
Explanation:
Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4
Note that the five elements can be returned in any order.
It does not matter what you leave beyond the returned k (hence they are underscores).

Constraints:
0 <= nums.length <= 100
0 <= nums[i] <= 50
0 <= val <= 100
"""

from typing import List, Callable


def remove_element(nums: List[int], val: int) -> int:
    """
    Remove all occurrences of val in nums in-place with fewer write operations.

    Args:
        nums (List[int]): The list of integers.
        val (int): The value to remove from the list.

    Returns:
        int: The number of elements in nums which are not equal to val.
    """
    left, right = 0, len(nums) - 1

    while left <= right:
        if nums[left] == val:
            nums[left] = nums[right]
            right -= 1
        else:
            left += 1

    return left


def test_function(function: Callable[[List[int], int], int]) -> None:
    """
    Test the function with the given input and expected output.
    """
    nums = [3, 2, 2, 3]
    val = 3
    expected_output = 2
    assert function(nums, val) == expected_output


if __name__ == "__main__":
    test_function(remove_element)
