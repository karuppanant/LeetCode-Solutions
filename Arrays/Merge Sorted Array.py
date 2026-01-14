Problem Number : 88
Problem Name : Merge Sorted Array
LeetCode Link : https://leetcode.com/problems/merge-sorted-array/submissions/1731242161/?envType=problem-list-v2&envId=array

Approach:
    Direct Copy + Sort Approach
    Copy all elements of nums2 into the remaining positions of nums1.
    Sort the combined array to maintain sorted order.
    This approach is simple but does not leverage the fact that both arrays are already sorted.

Complexity:
    Time Complexity: O((m+n) log(m+n))
    Space Complexity: O(1) (in-place, ignoring sort internals)

Program:
class Solution:
    def merge(self, nums1, m, nums2, n):
        nums1[m:]=nums2
        return nums1.sort()
