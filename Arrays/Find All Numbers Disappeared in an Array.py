Problem Number : 448
Problem Name : Find All Numbers Disappeared in an Array
LeetCode Link : https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/?envType=problem-list-v2&envId=array

Approach:
    In-Place Marking (Index as Hash) Approach
    Use the value of each element to mark the corresponding index as visited by making it negative.
    Traverse the array again to find indices that remain positive.
    Those indices represent numbers that did not appear in the array.

Complexity:
    Time Complexity: O(n)
    Space Complexity: O(1) (excluding output list)

Program:
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res=[]
        for i in range(len(nums)):
            index=abs(nums[i])-1
            nums[index]=-abs(nums[index])
        for i in range(len(nums)):
            if nums[i]>0:
                res.append(i+1)
        return res
