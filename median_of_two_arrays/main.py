"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

"""

def findMedianSortedArrays(nums1: list, nums2: list) -> float:
    nums = nums1 + nums2
    nums.sort()
    if len(nums) % 2 == 0:
        middle1 = len(nums) // 2 - 1
        middle2 = len(nums) // 2
        output = (float(nums[middle1]) + float(nums[middle2])) / 2

    else:
        middle = len(nums) // 2
        output = float(nums[middle])
    return output

def test_function(f):
    nums1 = [1, 3]
    nums2 = [2]
    assert f(nums1, nums2) == 2.0, f"Test case 1 failed: expected 2.0, got {f(nums1, nums2)}"

    nums1 = [1, 2]
    nums2 = [3, 4]
    assert f(nums1, nums2) == 2.5, f"Test case 2 failed: expected 2.5, got {f(nums1, nums2)}"

    nums1 = [1, 2]
    nums2 = [3, 4, 5]
    assert f(nums1, nums2) == 3.0, f"Test case 3 failed: expected 3.0 got {f(nums1, nums2)}"

    nums1 = []
    nums2 = [1]
    assert f(nums1, nums2) == 1.0, f"Test case 4 failed: expected 1.0, got {f(nums1, nums2)}"

    nums1 = [1]
    nums2 = [2]
    assert f(nums1, nums2) == 1.5, f"Test case 5 failed: expected 1.5, got {f(nums1, nums2)}"

    nums1 = [1, 2, 3]
    nums2 = [4, 5, 6, 7, 8, 9]
    assert f(nums1, nums2) == 5.0, f"Test case 6 failed: expected 5.0, got {f(nums1, nums2)}"

    print("All test cases passed!")

test_function(findMedianSortedArrays)
