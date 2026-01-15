Problem Number : 2348
Problem Name : Number of Zero-Filled Subarrays
LeetCode Link : https://leetcode.com/problems/number-of-zero-filled-subarrays/submissions/1881833275/?envType=problem-list-v2&envId=array

Approach:
    Counting Consecutive Zeros (Mathematical Formula)
    Traverse the array and count consecutive zeros.
    Maintain a count for consecutive zeros
    When a non-zero element is found:
    Add number of zero-filled subarrays using formula
    count × (count + 1) / 2
    Reset count to 0
    After traversal, add remaining zero subarrays (if array ends with zeros)
    This works because for k consecutive zeros, total subarrays = k(k+1)/2.

Complexity:
    Time Complexity: O(n)
    Space Complexity: O(1)

Program:
class Solution {
    public long zeroFilledSubarray(int[] nums) {
        int count=0;
        long result=0;
        for(int num:nums){
            if(num==0){
                count++;
            }else{
                result+=count*(count+1L)/2;
                count=0;
            }
        }
        result+=count*(count+1L)/2;
        return result;
    }
}
