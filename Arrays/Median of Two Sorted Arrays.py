Problem Number : 4
Problem Name : Median of Two Sorted Arrays
LeetCode Link : https://leetcode.com/problems/median-of-two-sorted-arrays/submissions/1791123381/?envType=problem-list-v2&envId=array

Approach : Binary Search on Partition (Optimized Approach)
Always apply binary search on the smaller array to reduce time complexity.
Partition both arrays such that left halves contain half of the total elements.
Adjust partitions until left-side max ≤ right-side min, then compute the median.

Complexity:
Time Complexity: O(log(min(n, m)))
Space Complexity: O(1)

Program:
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        len1, len2 = len(nums1), len(nums2)
        low, high = 0, len1
        total_half_length = (len1 + len2 + 1) // 2
        while low <= high:
            cut1 = (low + high) // 2
            cut2 = total_half_length - cut1
            l1 = nums1[cut1 - 1] if cut1 > 0 else float('-inf')
            r1 = nums1[cut1] if cut1 < len1 else float('inf')
            l2 = nums2[cut2 - 1] if cut2 > 0 else float('-inf')
            r2 = nums2[cut2] if cut2 < len2 else float('inf')
            if l1 <= r2 and l2 <= r1:
                if (len1 + len2) % 2 == 1:
                    return float(max(l1, l2))
                return (max(l1, l2) + min(r1, r2)) / 2.0
            elif l1 > r2:
                high = cut1 - 1
            else:
                low = cut1 + 1
        return 0.0
