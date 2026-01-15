Problem Number : 1089
Problem Name : Duplicate Zeros
LeetCode Link : https://leetcode.com/problems/duplicate-zeros/submissions/1796483539/?envType=problem-list-v2&envId=array

Approach:
    In-Place Shifting (Brute Force)
    Traverse the array from left to right.
    When a zero is found, shift all elements to the right by one position starting from the end.
    Skip the next index to avoid re-duplicating the inserted zero.

Complexity:
    Time Complexity: O(n²)
    Space Complexity: O(1)

Program:
class Solution {
    public void duplicateZeros(int[] arr) {
        int n=arr.length;
        for(int i=0;i<n;i++){
            if (arr[i]==0){
                for(int j=n-1;j>i;j--){
                    arr[j]=arr[j-1];
                }
                i++;
            }
        }
    }
}
