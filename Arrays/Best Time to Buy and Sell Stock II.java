Problem Number : 122
Problem Name : Best Time to Buy and Sell Stock II
LeetCode Link : https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/submissions/1881818261/?envType=problem-list-v2&envId=array

Approach:
    Greedy Approach
    Traverse the price array and capture every increasing price difference.
    Buy before a rise and sell at the peak by summing all positive consecutive differences.
    This effectively simulates multiple buy-sell transactions for maximum profit.

Complexity:
    Time Complexity: O(n)
    Space Complexity: O(1)

Program:
class Solution {
    public int maxProfit(int[] prices) {
        int n=prices.length;
        int max_profit=0;
        for(int i=1;i<n;i++){
            if(prices[i]>prices[i-1]){
                max_profit+=prices[i]-prices[i-1];
            }
        }
        return max_profit;
    }
}
