Problem Number : 2544
Problem Name : Alternating Digit Decomposition
LeetCode Link : https://leetcode.com/problems/compute-decimal-representation/submissions/1788388018/?envType=problem-list-v2&envId=array

Approach:
      Place Value Decomposition
      Traverse the number from least significant digit to most significant digit.
      For each digit:
      Multiply by its place value (1, 10, 100, …)
      Skip if the digit is 0
      Append non-zero components to result
      Reverse the list to maintain original left-to-right order.
      This decomposes the number into its non-zero place value components.

Complexity:
      Time Complexity: O(log n) (number of digits in n)
      Space Complexity: O(log n) (for result list)

Program:
class Solution:
    def decimalRepresentation(self, n):
        result=[]
        place=1
        while n>0:
            digit=n%10
            if digit!=0:
                result.append(digit*place)
            n=n//10
            place*=10
        return result[::-1]
