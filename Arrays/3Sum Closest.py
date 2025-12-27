Problem Number : 16
Problem Name : 3Sum Closest
LeetCode Link : https://leetcode.com/problems/3sum-closest/submissions/1865100321/?envType=problem-list-v2&envId=array

Approach:
Sorting + Two Pointer Approach:
      Sort the array to efficiently apply the two-pointer technique.
      Fix one element and move two pointers to find the sum closest to the target.
      Update the closest sum whenever a smaller difference is found.

Complexity:
      Time Complexity: O(n²)
      Space Complexity: O(1)

Program:
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n=len(nums)
        closest_sum=nums[0]+nums[1]+nums[2]
        for i in range(n-2):
            left=i+1
            right=n-1
            while left<right:
                curr_sum=nums[i]+nums[left]+nums[right]
                if abs(curr_sum - target) < abs(closest_sum - target):
                    closest_sum=curr_sum
                if curr_sum < target:
                    left+=1
                elif curr_sum > target:
                    right-=1
                else:
                    return curr_sum
        return closest_sum
