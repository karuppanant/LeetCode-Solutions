Problem Number : 303
Problem Name : Range Sum Query - Immutable
LeetCode Link : https://leetcode.com/problems/range-sum-query-immutable/submissions/1856514004/?envType=problem-list-v2&envId=array

Approach:
      Prefix Sum Approach
      Precompute the prefix sum array where prefix[i] stores the sum of the first i elements.
      To get the sum of any subarray [left, right], subtract prefix[left] from prefix[right + 1].
      Enables constant-time queries after linear-time preprocessing.

Complexity:
      Time Complexity: Initialization: O(n)
                      Query: O(1)
      Space Complexity: O(n)

Program:
class NumArray:
    def __init__(self, nums):
        self.prefix = [0]
        for i in range(len(nums)):
            self.prefix.append(self.prefix[i] + nums[i])
    def sumRange(self, left, right):
        return self.prefix[right + 1] - self.prefix[left]
