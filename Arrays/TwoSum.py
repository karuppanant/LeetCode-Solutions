Problem Number : 1
Problem Name : Two Sum
LeetCode Link : https://leetcode.com/problems/two-sum/submissions/1704341472/

Approach:
Brute Force Approach
  It checks all possible pairs of elements using nested loops.
  No extra data structures are used.
  Simple and straightforward, but not optimal for large inputs.

Complexity:
Time Complexity: O(n²)
Space Complexity: O(1)

Code:
class Solution:
    def twoSum(self,nums,target):
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return [i,j]
