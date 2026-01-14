Problem Number : 41
Problem Name : First Missing Positive
LeetCode Link : https://leetcode.com/problems/first-missing-positive/submissions/1865075096/?envType=problem-list-v2&envId=array

Approach:
    Cyclic Sort / Index Mapping Approach
    Place each positive number x (1 ≤ x ≤ n) at its correct index x-1.
    Rearrange elements in-place using swapping until every valid number is in its correct position.
    Scan the array to find the first index where nums[i] != i+1, which is the missing positive.

Complexity:
    Time Complexity: O(n)
    Space Complexity: O(1)

Program:
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n=len(nums)
        for i in range(n):
            while 1<=nums[i]<=n and nums[nums[i]-1] != nums[i]:
                nums[nums[i]-1],nums[i] = nums[i],nums[nums[i]-1]
        for i in range(n):
            if nums[i]!=i+1:
                return i+1 
        return n+1
