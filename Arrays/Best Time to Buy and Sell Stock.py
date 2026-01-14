Problem Number : 121
Problem Name : Best Time to Buy and Sell Stock
LeetCode Link : https://leetcode.com/problems/best-time-to-buy-and-sell-stock/submissions/1731290864/?envType=problem-list-v2&envId=array

Approach:
    Single Pass Greedy Approach
    Track the minimum price encountered so far while iterating through the array.
    At each step, calculate the profit if sold on that day and update the maximum profit.
    This ensures the buy happens before the sell.

Complexity:
    Time Complexity: O(n)
    Space Complexity: O(1)

Program:
class Solution:
    def maxProfit(self, prices):
        min_price=float('inf')
        max_price=0
        for price in prices:
            min_price=min(min_price,price)
            max_price=max(max_price,price-min_price)
        return max_price
