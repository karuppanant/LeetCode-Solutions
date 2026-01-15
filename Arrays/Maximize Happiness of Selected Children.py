Problem Number : 2844
Problem Name : Maximum Happiness Sum
LeetCode Link : https://leetcode.com/problems/maximize-happiness-of-selected-children/submissions/1865063453/?envType=problem-list-v2&envId=array

Approach:
      Greedy + Sorting
      Sort happiness array in descending order.
      Iterate over the first k elements:
      Calculate curr = happiness[i] - i
      If curr > 0, add it to the result res
      Stop if curr <= 0 since further values will not contribute positively
      Return the total res.
      This approach prioritizes largest happiness values and accounts for the decreasing effect of the index i.

Complexity:
      Time Complexity: O(n log n) (sorting)
      Space Complexity: O(1)

Program:
class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        res = 0
        for i in range(k):
            curr = happiness[i] - i
            if curr > 0:
                res += curr
            else:
                break
        return res
