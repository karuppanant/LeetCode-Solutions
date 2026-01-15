Problem Number : 840
Problem Name : Magic Squares In Grid
LeetCode Link : https://leetcode.com/problems/magic-squares-in-grid/submissions/1869463802/?envType=problem-list-v2&envId=array

Approach:
    Brute Force + Property-Based Validation
    Iterate over every possible 3×3 subgrid in the matrix.
    Use the property that a 3×3 magic square must contain numbers 1–9 exactly once and have 5 at the center.
    Validate all rows, columns, and diagonals sum to 15.

Complexity:
    Time Complexity: O(m × n)
    Space Complexity: O(1)

Program:
class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        row,col=len(grid),len(grid[0])
        count=0
        for i in range(row-2):
            for j in range(col-2):
                if grid[i+1][j+1]!=5:
                    continue
                a=grid[i][j]
                b=grid[i][j+1]
                c=grid[i][j+2]
                d=grid[i+1][j]
                e=grid[i+1][j+1]
                f=grid[i+1][j+2]
                g=grid[i+2][j]
                h=grid[i+2][j+1]
                k=grid[i+2][j+2]
                nums=[a,b,c,d,e,f,g,h,k]
                if set(nums)!=set(range(1,10)):
                    continue
                if (a+b+c==15 and d+e+f==15 and g+h+k==15 and a+d+g==15 and b+e+h==15 and c+f+k==15 and a+e+k==15 and c+e+g==15):
                    count+=1
        return count
