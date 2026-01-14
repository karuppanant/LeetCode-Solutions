Problem Number : 169
Problem Name : Majority Element
LeetCode Link : https://leetcode.com/problems/majority-element/submissions/1732549291/?envType=problem-list-v2&envId=array

Approach:
    Sorting-Based Approach
    Sort the array so identical elements are grouped together.
    Since the majority element appears more than ⌊n/2⌋ times, it must occupy the middle index.
    Return the element at index n//2.

Complexity:
    Time Complexity: O(n log n)
    Space Complexity: O(1) (ignoring sort internals)

Program:
class Solution:
    def majorityElement(self, nums):
        nums.sort()
        return nums[len(nums)//2]
