Problem Number : 66
Problem Name : Plus One
LeetCode Link : https://leetcode.com/problems/plus-one/submissions/1870999991/?envType=problem-list-v2&envId=array

Approach:
    String Conversion Approach
    Convert the list of digits into a string and then into an integer.
    Increment the integer by one.
    Convert the result back into a list of digits.

Complexity:
    Time Complexity: O(n)
    Space Complexity: O(n)

Program:
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num=int("".join(map(str,digits)))
        num+=1
        return [int(d) for d in str(num)]
