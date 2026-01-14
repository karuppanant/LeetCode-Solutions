Problem Number : 350
Problem Name : Intersection of Two Arrays II
LeetCode Link : https://leetcode.com/problems/intersection-of-two-arrays-ii/submissions/1857281331/?envType=problem-list-v2&envId=array

Approach:
    Sorting + Two Pointer Approach
    Sort both input arrays to enable linear comparison.
    Use two pointers to traverse the arrays and compare elements.
    When elements match, add to result and move both pointers; otherwise move the pointer with the smaller value.

Complexity:
    Time Complexity: O(n log n + m log m)
    Space Complexity: O(1) (excluding output list)

Program:
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        res=[]
        i=0
        j=0
        while i<len(nums1) and j<len(nums2):
            if nums1[i]==nums2[j]:
                res.append(nums1[i])
                i+=1
                j+=1
            elif nums1[i]<nums2[j]:
                i+=1
            else:
                j+=1
        return res
