Problem Number : 119
Problem Name : Pascal’s Triangle II
LeetCode Link : https://leetcode.com/problems/pascals-triangle-ii/submissions/1741006650/?envType=problem-list-v2&envId=array

Approach:
    Iterative Row Construction (Optimized Space)
    Start with the first row [1].
    Repeatedly generate the next row using only the current row values.
    Build up to the required rowIndex without storing the entire triangle.

Complexity:
    Time Complexity: O(k²) (k = rowIndex)
    Space Complexity: O(k)

Program:
class Solution:
    def getRow(self, rowIndex):
        row=[1]
        for _ in range(rowIndex):
            row=[1]+[row[i]+row[i+1] for i in range(len(row)-1)]+[1]
        return row
