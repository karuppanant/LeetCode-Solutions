Problem Number : 349
Problem Name : Intersection of Two Arrays
LeetCode Link : https://leetcode.com/problems/intersection-of-two-arrays/submissions/1856314376/?envType=problem-list-v2&envId=array

Approach:
    Set-Based Approach
    Convert both arrays into sets to remove duplicates.
    Iterate through one set and check if elements exist in the other set.
    Store common elements in the result list.

Complexity:
    Time Complexity: O(n + m)
    Space Complexity: O(n + m)

Program:
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1=set(nums1)
        nums2=set(nums2)
        res=[]
        for i in nums1:
            if i in nums2:
                res.append(i)
        return res
