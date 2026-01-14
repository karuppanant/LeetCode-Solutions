Problem Number : 238
Problem Name : Product of Array Except Self
LeetCode Link : https://leetcode.com/problems/product-of-array-except-self/submissions/1881805929/?envType=problem-list-v2&envId=array

Approach:
    Prefix and Suffix Product (Optimized)
    First pass: compute the prefix product for each element and store it in the output array.
    Second pass (right to left): maintain a running suffix product and multiply it with the prefix product in the output array.
    Avoids using division and achieves O(1) extra space (excluding output array).

Complexity:
    Time Complexity: O(n)
    Space Complexity: O(1) (excluding output array)

Program:
class Solution {
    public int[] productExceptSelf(int[] nums) {
        int n=nums.length;
        int[] output=new int[n];
        output[0]=1;
        for(int i=1;i<n;i++){
            output[i]=output[i-1]*nums[i-1];
        }
        int right=1;
        for(int i=n-1;i>=0;i--){
            output[i]*=right;
            right*=nums[i];
        }
        return output;
    }
}
