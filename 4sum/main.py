"""
Given an array nums of n integers, return an array of all the unique quadruplets
[nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.



Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
Example 2:

Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]


Constraints:

1 <= nums.length <= 200
-109 <= nums[i] <= 109
-109 <= target <= 109
"""

# pylint:disable=invalid-name


def fourSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    """
    nums.sort()
    results = []
    length = len(nums)

    for i in range(length - 3):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        if nums[i] * 4 > target:
            break

        for j in range(i + 1, length - 2):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            if nums[i] + nums[j] * 3 > target:
                break
            l, r = j + 1, length - 1
            while l < r:
                total = nums[i] + nums[j] + nums[l] + nums[r]

                if total == target:
                    results.append([nums[i], nums[j], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
                elif total < target:
                    l += 1
                else:
                    r -= 1
    return results


def test_function(f):
    """
    Testing 4sum
    """
    assert f([1, 0, -1, 0, -2, 2], 0) == [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
    assert f([2, 2, 2, 2, 2], 8) == [[2, 2, 2, 2]]


if __name__ == "__main__":
    test_function(fourSum)
