Problem Number : 976
Problem Name : Largest Perimeter Triangle
LeetCode Link : https://leetcode.com/problems/largest-perimeter-triangle/submissions/1784951699/?envType=problem-list-v2&envId=array

Approach:
    Sorting + Greedy Approach
    Sort the array in ascending order.
    Traverse from the largest elements backward and check the triangle inequality.
    The first valid triplet encountered gives the maximum possible perimeter.

Complexity:
    Time Complexity: O(n log n)
    Space Complexity: O(1) (excluding sorting overhead)

Program:
class Solution:
    def largestPerimeter(self, nums):
        nums.sort()
        for i in range(len(nums)-1,1,-1):
            if nums[i-2]+nums[i-1]>nums[i]:
                return nums[i-2]+nums[i-1]+nums[i]
        return 0
