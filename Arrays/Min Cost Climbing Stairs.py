Problem Number : 746
Problem Name : Min Cost Climbing Stairs
LeetCode Link : https://leetcode.com/problems/min-cost-climbing-stairs/submissions/1776079595/?envType=problem-list-v2&envId=array

Approach:
      Dynamic Programming (Space Optimized)
      Each step’s minimum cost depends on the minimum cost of the previous two steps.
      Use two variables to store the minimum cost to reach the last two steps.
      Iteratively compute the current cost and update the variables.

Complexity:
      Time Complexity: O(n)
      Space Complexity: O(1)

Program:
class Solution:
    def minCostClimbingStairs(self,cost):
        n=len(cost)
        prev,prev_n=cost[0],cost[1]
        for i in range(2,n):
            current=cost[i]+min(prev,prev_n)
            prev,prev_n=prev_n,current
        return min(prev,prev_n)
