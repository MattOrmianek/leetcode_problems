"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]

Constraints:
1 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
"""
# This solution is O(n^2) because of use two loops
def two_sum(nums: list, target: int) -> list:
    for first in range(len(nums)):
        for second in range(len(nums)):
            first_index = first
            second_index = second
            first_number = nums[first]
            second_number = nums[second]
            if first_index != second_index and first_number + second_number == target:
                return [first_index, second_index]


# For reducing complexity we can use hash map

def two_sum_better(nums: list, target: int) -> list:
    num_to_index = {}
    for index, number in enumerate(nums):
        complement = target - number
        if complement in num_to_index:
            return [num_to_index[complement], index]
        num_to_index[number] = index


def test_function(f):
    nums = [2, 7, 11, 15]
    target = 9
    assert f(nums, target) == [0, 1], "Test case 1 failed"

    nums = [3, 2, 4]
    target = 6
    assert f(nums, target) == [1, 2], "Test case 2 failed"

    nums = [3, 3]
    target = 6
    assert f(nums, target) == [0, 1], "Test case 3 failed"

    nums = [1, 2]
    target = 10
    assert f(nums, target) is None, "Test case 4 failed"


test_function(two_sum)
test_function(two_sum_better)
