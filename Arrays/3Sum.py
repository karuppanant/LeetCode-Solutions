Problem Number : 15
Problem Name : 3Sum
LeetCode Link : https://leetcode.com/problems/3sum/submissions/1856436853/?envType=problem-list-v2&envId=array

Approach:
Sorting + Two Pointer Approach
      Sort the array to efficiently handle duplicates and enable two-pointer traversal.
      Fix one element and use two pointers to find pairs whose sum equals the negative of the fixed element.
      Skip duplicate elements to ensure unique triplets in the result.

Complexity:
    Time Complexity: O(n²)
    Space Complexity: O(1) (excluding output list)

Program:
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        n=len(nums)
        nums.sort()
        for i in range(n):
            if i>0 and nums[i]==nums[i-1]:
                continue
            left,right=i+1,n-1
            while left<right:
                total=nums[i]+nums[left]+nums[right]
                if total==0:
                    res.append([nums[i],nums[left],nums[right]])
                    while left<right and nums[left]==nums[left+1]:
                        left+=1
                    while left<right and nums[right]==nums[right-1]:
                        right-=1
                    left+=1
                    right-=1
                elif total<0:
                    left+=1
                else:
                    right-=1
        return res
