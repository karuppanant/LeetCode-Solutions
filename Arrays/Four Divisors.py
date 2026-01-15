Problem Number : 1390
Problem Name : Four Divisors
LeetCode Link : https://leetcode.com/problems/four-divisors/submissions/1874367045/?envType=problem-list-v2&envId=array

Approach:
      Divisor Enumeration up to √n (Early Exit Optimization)
      For each number n in nums, find all its divisors.
      Iterate from 1 to √n:
      If i divides n, add both i and n//i to a set.
      If the divisor count exceeds 4, stop early (not valid).
      If exactly 4 distinct divisors are found, return their sum.
      Accumulate the sum for all valid numbers.
      This efficiently avoids unnecessary checks.

Complexity:
      Time Complexity: O(k × √n)
                       where k = number of elements in nums
      Space Complexity: O(1) (divisor set size ≤ 4)

Program:
class Solution:
    def sumFourDivisors(self, nums):
        def get_sum(n):
            divs = set()
            for i in range(1, int(n**0.5) + 1):
                if n % i == 0:
                    divs.add(i)
                    divs.add(n // i)
                if len(divs) > 4:
                    return 0
            return sum(divs) if len(divs) == 4 else 0

        ans = 0
        for n in nums:
            ans += get_sum(n)
        return ans 
