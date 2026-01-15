Problem Number : 2799
Problem Name : Minimum Number of Boxes to Store Apples
LeetCode Link : https://leetcode.com/problems/apple-redistribution-into-boxes/submissions/1864255732/?envType=problem-list-v2&envId=array

Approach:
      Greedy Approach with Sorting
      Calculate total_apples by summing all apples.
      Sort capacity in descending order.
      Start filling boxes from largest capacity:
      Add box capacity to curr (current stored apples)
      Increment boxes count
      Stop once curr >= total_apples
      Return the number of boxes used.
      This ensures minimum boxes are used by filling largest capacities first.

Complexity:
      Time Complexity: O(n log n) (for sorting)
      Space Complexity: O(1)

Program:
class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        total_apples=sum(apple)
        capacity.sort(reverse=True)
        curr=0
        boxes=0
        for c in capacity:
            curr+=c
            boxes+=1
            if curr>=total_apples:
                return boxes
