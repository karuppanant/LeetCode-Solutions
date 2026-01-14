Problem Number : 108
Problem Name : Convert Sorted Array to Binary Search Tree
LeetCode Link : https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/submissions/1731268214/?envType=problem-list-v2&envId=array

Approach:
    Divide and Conquer / Recursive Approach
    Choose the middle element of the sorted array as the root to ensure balance.
    Recursively apply the same logic to the left and right subarrays.
    This guarantees a height-balanced Binary Search Tree.

Complexity:
    Time Complexity: O(n)
    Space Complexity: O(log n) (recursive call stack for balanced tree)

Program:
class Solution:
    def sortedArrayToBST(self, nums):
        if not nums:
            return None
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        return root
