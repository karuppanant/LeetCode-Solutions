Problem Number : 485
Problem Name : Max Consecutive Ones
LeetCode Link : https://leetcode.com/problems/max-consecutive-ones/submissions/1795440613/?envType=problem-list-v2&envId=array

Approach:
    Single Pass Counting Approach
    Traverse the array while maintaining a counter for consecutive 1s.
    Reset the counter when a 0 is encountered and update the maximum count.
    Return the maximum consecutive count found.

Complexity:
    Time Complexity: O(n)
    Space Complexity: O(1)

Program:
class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int max_count=0;
        int current_count=0;
        for(int num:nums){
            if(num==1){
                current_count++;
            }else{
                max_count=Math.max(max_count,current_count);
                current_count=0;
            }
        }
        max_count=Math.max(max_count,current_count);
        return max_count;
    }
}
