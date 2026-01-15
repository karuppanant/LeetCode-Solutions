Problem Number : 961
Problem Name : N-Repeated Element in Size 2N Array
LeetCode Link : https://leetcode.com/problems/n-repeated-element-in-size-2n-array/?envType=problem-list-v2&envId=array

Approach:
    Hash Set Approach
    Use a set to keep track of elements already seen.
    Traverse the array and return the element when it is encountered again.
    Since one element is repeated N times, the first duplicate found is the answer.

Complexity:
    Time Complexity: O(n)
    Space Complexity: O(n)

Program:
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n=len(nums)
        seen=set()
        ans=0
        for i in range(n):
            if nums[i] in seen:
                ans=nums[i]
            seen.add(nums[i])
        return ans
