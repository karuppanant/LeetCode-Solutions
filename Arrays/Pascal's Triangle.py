Problem Number : 118
Problem Name : Pascal’s Triangle
LeetCode Link : https://leetcode.com/problems/pascals-triangle/submissions/1740912149/?envType=problem-list-v2&envId=array

Approach:
    Dynamic Programming / Row-by-Row Construction
    Start with the first row [1] as the base case.
    Each new row is built using values from the previous row: inner elements are sums of adjacent elements.
    Append 1 at both ends of every row.

Complexity:
    Time Complexity: O(n²)
    Space Complexity: O(n²)

Program:
class Solution:
    def generate(self,numRows):
        res=[[1]]
        for _ in range(numRows-1):
            prev=res[-1]
            row=[1]+[prev[i]+prev[i+1] for i in range(len(prev)-1)]+[1] 
            res.append(row)
        return res
