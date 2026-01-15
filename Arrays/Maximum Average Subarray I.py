Problem Number : 643
Problem Name : Maximum Average Subarray I
LeetCode Link : https://leetcode.com/problems/maximum-average-subarray-i/submissions/1857399149/?envType=problem-list-v2&envId=array

Approach:
Sliding Window Approach
Calculate the sum of the first window of size k.
Slide the window by adding the next element and removing the element leaving the window.
Track the maximum window sum and compute the average.

Complexity:
Time Complexity: O(n)
Space Complexity: O(1)

Program:
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum=sum(nums[:k])
        max_sum=window_sum
        for i in range(k,len(nums)):
            window_sum+=nums[i]-nums[i-k]
            max_sum=max(window_sum,max_sum)
        return max_sum/k
