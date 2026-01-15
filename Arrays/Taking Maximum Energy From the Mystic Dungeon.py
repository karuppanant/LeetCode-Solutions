Problem Number : 2816
Problem Name : Maximum Energy You Can Obtain from Boxes
LeetCode Link : https://leetcode.com/problems/taking-maximum-energy-from-the-mystic-dungeon/submissions/1797347040/?envType=problem-list-v2&envId=array

Approach:
      Dynamic Programming (Bottom-Up)
      Let dp[i] represent the maximum energy obtainable starting from box i.
      Traverse from the end (i = n-1 to 0):
      Base energy: dp[i] = energy[i]
      If i + k < n, we can jump k steps → add dp[i + k] to dp[i].
      Track the maximum energy overall while filling dp.
      Return the maximum value obtained from any starting index.
      This is an efficient DP solution using bottom-up calculation.

Complexity:
      Time Complexity: O(n)
      Space Complexity: O(n)

Program:
class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        n=len(energy)
        dp=[0]*n
        max_overall_energy=float('-inf')
        for i in range(n-1,-1,-1):
            dp[i]=energy[i]
            if i+k <n:
                dp[i]+=dp[i+k]
            max_overall_energy=max(max_overall_energy,dp[i])
        return max_overall_energy
