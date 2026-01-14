Problem Number : 189
Problem Name : Rotate Array
LeetCode Link : https://leetcode.com/problems/rotate-array/submissions/1881791158/?envType=problem-list-v2&envId=array

Approach:
    Array Reversal Technique
    Normalize k using modulo to handle cases where k > n.
    Reverse the entire array, then reverse the first k elements.
    Reverse the remaining elements to achieve the final rotated array.

Complexity:
    Time Complexity: O(n)
    Space Complexity: O(1)

Program:
class Solution {
    public void rotate(int[] nums, int k) {
        int n=nums.length;
        k=k%n;
        reverse(nums,0,n-1);
        reverse(nums,0,k-1);
        reverse(nums,k,n-1);
    }
    private void reverse(int[] nums,int start,int end){
        while(start<end){
        int temp=nums[start];
        nums[start]=nums[end];
        nums[end]=temp;
        start++;
        end--;
        }
    }
}
