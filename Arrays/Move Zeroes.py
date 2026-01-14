Problem Number : 283
Problem Name : Move Zeroes
LeetCode Link : https://leetcode.com/problems/move-zeroes/submissions/1856308860/?envType=problem-list-v2&envId=array

Approach:
    Extra Space Approach
    Separate the array into two lists: one for non-zero elements and one for zeros.
    Concatenate non-zero elements with zeros and update the original array in-place.

Complexity:
    Time Complexity: O(n)
    Space Complexity: O(n) (due to extra lists)

Program:
class Solution:
    def moveZeroes(self, nums):
        zeros = []
        nonzeros = []
        for i in nums:
            if i == 0:
                zeros.append(0)
            else:
                nonzeros.append(i)
        nums[:] = nonzeros + zeros
