Problem Number : 812
Problem Name : Largest Triangle Area
LeetCode Link : https://leetcode.com/problems/largest-triangle-area/submissions/1784230581/?envType=problem-list-v2&envId=array

Approach:
    Brute Force + Geometry (Shoelace Formula)
    Generate all possible combinations of three points.
    Compute the area of the triangle formed by each triplet using the shoelace formula.
    Track and return the maximum area found.

Complexity:
    Time Complexity: O(n³)
    Space Complexity: O(1)

Program:
from itertools import combinations
class Solution:
    def largestTriangleArea(self, points):
        max_area=0
        for (x1,y1),(x2,y2),(x3,y3) in combinations(points,3):
            area=abs(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2))/2
            max_area=max(max_area,area)
        return max_area
