Problem Number : 2529
Problem Name : Maximum Count of Positive or Negative Numbers
LeetCode Link : https://leetcode.com/problems/maximum-count-of-positive-integer-and-negative-integer/submissions/1748545687/?envType=problem-list-v2&envId=array

Approach:
    Simple Counting
    Initialize counters for positive (pos) and negative (neg) numbers.
    Traverse the array:
    Increment pos if number > 0
    Increment neg if number < 0
    Return the maximum of pos and neg.

Complexity:
    Time Complexity: O(n)
    Space Complexity: O(1)

Program:
class Solution:
    def maximumCount(self, nums):
        pos=0
        neg=0
        for i in nums:
            if i>0:
                pos+=1
            elif i<0:
                neg+=1
        return max(pos,neg)
