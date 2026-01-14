Problem Number : 414
Problem Name : Third Maximum Number
LeetCode Link : https://leetcode.com/problems/third-maximum-number/submissions/1732592543/?envType=problem-list-v2&envId=array

Approach:
    Set + Sorting Approach
    Convert the array to a set to remove duplicate elements.
    Sort the unique elements in descending order.
    Return the third maximum if it exists; otherwise, return the maximum.

Complexity:
    Time Complexity: O(n log n)
    Space Complexity: O(n)

Program:
class Solution:
    def thirdMax(self, nums):
        nums=list(set(nums))
        nums.sort(reverse=True)
        if len(nums)<3:
            return nums[0]
        return nums[2]
