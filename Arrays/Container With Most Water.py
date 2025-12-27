Problem Number : 11
Problem Name : Container With Most Water
LeetCode Link : https://leetcode.com/problems/container-with-most-water/submissions/1790903627/?envType=problem-list-v2&envId=array

Approach:
Two Pointer Approach (Greedy Optimization)
  Start with two pointers at the beginning and end of the array.
  Calculate the area formed and move the pointer with the smaller height to maximize possible area.
  Continue until both pointers meet, keeping track of the maximum area.

Complexity:
Time Complexity: O(n)
Space Complexity: O(1)

Program:
class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        left = 0
        right = n - 1
        max_area = 0
        while left < right:
            current_height = min(height[left], height[right])
            width = right - left
            current_area = current_height * width
            max_area = max(max_area, current_area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area
