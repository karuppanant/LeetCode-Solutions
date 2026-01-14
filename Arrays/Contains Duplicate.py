Problem Number : 217
Problem Name : Contains Duplicate
LeetCode Link : https://leetcode.com/problems/contains-duplicate/submissions/1732558770/?envType=problem-list-v2&envId=array

Approach:
    Hash Set Approach
    Convert the array into a set to remove duplicate elements.
    Compare the length of the set with the original array.
    If lengths differ, duplicates exist.

Complexity:
    Time Complexity: O(n)
    Space Complexity: O(n)

Program:
class Solution:
    def containsDuplicate(self, nums):
        return len(nums)!=len(set(nums))
