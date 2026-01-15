Problem Number : 2785
Problem Name : Maximum Number of Distinct Elements After K Increments
LeetCode Link : https://leetcode.com/problems/maximum-number-of-distinct-elements-after-operations/submissions/1805123113/?envType=problem-list-v2&envId=array

Approach:
      Greedy + Sorting
      Sort the array to process numbers in order.
      Maintain next_available → the next number we can assign to keep elements distinct.
      For each num:
      Calculate assign = max(next_available, num - k) → earliest possible value we can assign within k increments/decrements.
      If assign <= num + k → valid assignment:
      Increment distinct_count
      Update next_available = assign + 1
      Return distinct_count after processing all numbers.
      This ensures maximum distinct elements by greedily assigning the smallest available values.

Complexity:
      Time Complexity: O(n log n) (for sorting)  
      Space Complexity: O(1)

Program:
from typing import List
class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()         
        next_available = float('-inf')
        distinct_count = 0
        for num in nums:
            assign = max(next_available, num - k) 
            if assign <= num + k:
                distinct_count += 1
                next_available = assign + 1      
        return distinct_count
