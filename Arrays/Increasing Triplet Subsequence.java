Problem Number : 334
Problem Name : Increasing Triplet Subsequence
LeetCode Link : https://leetcode.com/problems/increasing-triplet-subsequence/submissions/1881847953/?envType=problem-list-v2&envId=array

Approach:
    Greedy Approach (Two Variables Tracking)
    Maintain two variables first and second to store the smallest and second smallest values seen so far.
    Traverse the array and update these values when a smaller number is found.
    If a number greater than both first and second is found, an increasing triplet exists.

Complexity:
    Time Complexity: O(n)
    Space Complexity: O(1)

Program:
class Solution {
    public boolean increasingTriplet(int[] nums) {
        int first=Integer.MAX_VALUE;
        int second=Integer.MAX_VALUE;
        for(int num:nums){
            if(num<=first){
                first=num;
            }else if(num<=second){
                second=num;
            }else{
                return true;
            }
        }
        return false;
    }
}
