Problem Number : 2857
Problem Name : Check for Increasing Subarrays of Length K
LeetCode Link : https://leetcode.com/problems/adjacent-increasing-subarrays-detection-i/submissions/1801571034/?envType=problem-list-v2&envId=array

Approach:
      Sliding Window + Brute Force Check
      Traverse the array from index 0 to n - 2 * k:
      Check the first subarray of length k for strictly increasing order.
      Check the second subarray of length k (immediately after the first) for strictly increasing order.
      If both subarrays are strictly increasing → return true.
      If no such pair of subarrays is found → return false.
      This is a simple brute-force approach suitable for moderate array sizes.

Complexity:
      Time Complexity: O(n × k)    
      Space Complexity: O(1)

Program:
class Solution {
    public boolean hasIncreasingSubarrays(List<Integer> nums, int k) {
        int n = nums.size();
        
        for (int i = 0; i <= n - 2 * k; i++) {
            boolean firstIncreasing = true;
            for (int j = i; j < i + k - 1; j++) {
                if (nums.get(j) >= nums.get(j + 1)) {
                    firstIncreasing = false;
                    break;
                }
            }
            
            boolean secondIncreasing = true;
            for (int j = i + k; j < i + 2 * k - 1; j++) {
                if (nums.get(j) >= nums.get(j + 1)) {
                    secondIncreasing = false;
                    break;
                }
            }
            
            if (firstIncreasing && secondIncreasing) {
                return true;
            }
        }
        
        return false;
    }
}
