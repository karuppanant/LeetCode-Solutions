Problem Number : 1351
Problem Name : Count Negative Numbers in a Sorted Matrix
LeetCode Link : https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/?envType=problem-list-v2&envId=array

Approach:
    Flatten + Count (Simple & Readable)
    Use itertools.chain.from_iterable() to flatten the 2D matrix into a single sequence.
    Iterate through all values.
    Increment count whenever a value is negative (< 0).
    This approach ignores the sorted property of the matrix but is very easy to understand and implement.

Complexity:
    Time Complexity: O(m × n)
    Space Complexity: O(1) (ignoring iterator overhead)

Program:
from itertools import chain
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count=0
        for val in chain.from_iterable(grid):
            if val<0:
                count+=1
        return count
