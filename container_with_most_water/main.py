"""
You are given an integer array height of length n.
There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.
"""
def maxArea(height):
    max_area = 0
    left = 0
    right = len(height) - 1
    while left < right:
        if height[left] <= height[right]:
            area = height[left] * (right - left)
            left += 1
        else:
            area = height[right] * (right - left)
            right -= 1
        if area > max_area:
            max_area = area

    return max_area


def test_function(f):
    assert f([1,8,6,2,5,4,8,3,7]) == 49, "Test case 1 failed"
    assert f([1,2]) == 1, "Test case 2 failed"
    assert f([4,3,2,1,4]) == 16, "Test case 3 failed"

test_function(maxArea)
