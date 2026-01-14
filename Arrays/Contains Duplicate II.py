Problem Number : 219
Problem Name : Contains Duplicate II
LeetCode Link : https://leetcode.com/problems/contains-duplicate-ii/submissions/1791086443/?envType=problem-list-v2&envId=array

Approach:
    Hash Map (Index Tracking) Approach
    Use a hash map to store each number and its most recent index.
    While traversing, check if the same number has appeared before within distance k.
    Update the index in the map to always keep the latest occurrence.

Complexity:
    Time Complexity: O(n)
    Space Complexity: O(n)

Program:
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        num_to_index={}
        for i,num in enumerate(nums):
            if num in num_to_index:
                prev_index=num_to_index[num]
                a_d=abs(i-prev_index)
                if a_d <=k:
                    return True
            num_to_index[num]=i
        return False
