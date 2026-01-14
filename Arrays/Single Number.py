Problem Number : 136
Problem Name : Single Number
LeetCode Link : https://leetcode.com/problems/single-number/submissions/1732543488/?envType=problem-list-v2&envId=array

Approach:
    Bit Manipulation (XOR Approach)
    Use the XOR operator on all elements of the array.
    Duplicate numbers cancel out because a ^ a = 0.
    The remaining value after all XOR operations is the single number.

Complexity:
    Time Complexity: O(n)
    Space Complexity: O(1)

Program:
class Solution:
    def singleNumber(self, nums):
        result=0
        for num in nums:
            result^=num
        return result
