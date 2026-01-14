Problem Number : 268
Problem Name : Missing Number
LeetCode Link : https://leetcode.com/problems/missing-number/submissions/1732574021/?envType=problem-list-v2&envId=array

Approach:
    Mathematical Sum Formula Approach
    Calculate the sum of the first n natural numbers using n*(n+1)/2.
    Subtract the sum of elements in the array from this expected sum to find the missing number.

Complexity:
    Time Complexity: O(n)
    Space Complexity: O(1)

Program:
class Solution:
    def missingNumber(self, nums):
        n = len(nums)
        expected_sum = n * (n + 1) // 2
        return expected_sum - sum(nums)
