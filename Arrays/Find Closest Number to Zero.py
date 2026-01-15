Problem Number : 2239
Problem Name : Find Closest Number to Zero
LeetCode Link : https://leetcode.com/problems/find-closest-number-to-zero/submissions/1756594521/?envType=problem-list-v2&envId=array

Approach:
Built-in min() with custom key
We want:
The number with minimum absolute value
If there is a tie (e.g., -2 and 2), choose the positive number
This is achieved by the key:
(abs(x), -x)
abs(x) → closest to zero
-x → prefers positive values when absolute values are equal

Complexity:
Time: O(n)
Space: O(1)

Program:
class Solution:
    def findClosestNumber(self, nums):
        return min(nums, key=lambda x: (abs(x), -x))
