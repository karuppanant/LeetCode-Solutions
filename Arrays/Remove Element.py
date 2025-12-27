Problem Number : 27
Problem Name : Remove Element
LeetCode Link : https://leetcode.com/problems/remove-element/submissions/1730185789/?envType=problem-list-v2&envId=array

Approach:
Two Pointer Approach
      Use one pointer i to track the index for placing valid elements.
      Traverse the array with pointer j and copy elements that are not equal to val.
      Return i as the new length after in-place modification.

Complexity:
      Time Complexity: O(n)
      Space Complexity: O(1)

Program:
class Solution:
    def removeElement(self, nums, val):
        if not nums:
            return 0
        i = 0 
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i
