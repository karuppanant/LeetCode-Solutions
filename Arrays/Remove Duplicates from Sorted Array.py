Problem Number : 26
Problem Name : Remove Duplicates from Sorted Array
LeetCode Link : https://leetcode.com/problems/remove-duplicates-from-sorted-array/submissions/1729734833/?envType=problem-list-v2&envId=array

Approach:
Two Pointer Approach
      Maintain one pointer i for the position of the last unique element.
      Traverse the array using pointer j and compare it with nums[i].
      When a new unique value is found, increment i and place the value at index i.

Complexity:
      Time Complexity: O(n)
      Space Complexity: O(1)

Program:
class Solution:
    def removeDuplicates(self,nums):
        if not nums:
            return 0
        i=0
        for j in range(0,len(nums)):
            if nums[j]!=nums[i]:
                i+=1
                nums[i]=nums[j]
        return i+1
