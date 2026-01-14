Problem Number : 35
Problem Name : Search Insert Position
LeetCode Link : https://leetcode.com/problems/search-insert-position/submissions/1730232583/?envType=problem-list-v2&envId=array

Approach:
    Linear Search Approach
    Traverse the array from the beginning.
    Return the index as soon as an element greater than or equal to the target is found.
    If no such element exists, return the array length as the insertion position.

Complexity:
    Time Complexity: O(n)
    Space Complexity: O(1)

Program:
class Solution:
    def searchInsert(self, nums, target):
        for i in range(len(nums)):
            if nums[i] >= target:
                return i
        return len(nums)
