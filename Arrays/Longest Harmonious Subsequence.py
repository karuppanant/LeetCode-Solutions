Problem Number : 594
Problem Name : Longest Harmonious Subsequence
LeetCode Link : https://leetcode.com/problems/longest-harmonious-subsequence/submissions/1857378570/?envType=problem-list-v2&envId=array

Approach:
      Sorting + Sliding Window (Two Pointer) Approach
      Sort the array so that elements with small differences are adjacent.
      Use two pointers to maintain a window where the difference between max and min is at most 1.
      Update the longest length when the difference is exactly 1.

Complexity:
      Time Complexity: O(n log n)
      Space Complexity: O(1) (excluding sorting overhead)

Program:
from collections import Counter
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums.sort()
        left=0
        longest=0
        for right in range(len(nums)):
            while nums[right]-nums[left]>1:
                left+=1
            if nums[right]-nums[left]==1:
                longest=max(longest,right-left+1)
        return longest
