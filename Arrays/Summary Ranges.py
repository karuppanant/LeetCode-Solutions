Problem Number : 228
Problem Name : Summary Ranges
LeetCode Link : https://leetcode.com/problems/summary-ranges/submissions/1856294637/?envType=problem-list-v2&envId=array

Approach:
    Two Pointer / Range Tracking Approach
    Use two pointers i and j to track the start and end of consecutive sequences.
    Expand j while numbers are consecutive.
    Add a single number or a range "start->end" to the result list and move i to j + 1.

Complexity:
    Time Complexity: O(n)
    Space Complexity: O(1) (excluding output list)

Program:
class Solution:
    def summaryRanges(self, nums):
        res = []
        i = 0
        while i < len(nums):
            j = i
            while j + 1 < len(nums) and nums[j + 1] == nums[j] + 1:
                j += 1
            res.append(str(nums[i]) if i == j else f"{nums[i]}->{nums[j]}")
            i = j + 1
        return res
