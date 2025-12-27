Problem Number : 14
Problem Name : Longest Common Prefix
LeetCode Link : https://leetcode.com/problems/longest-common-prefix/submissions/1704939457/?envType=problem-list-v2&envId=array

Approach:
Horizontal Scanning Approach
      Initialize the prefix as the first string in the list.
      Compare the prefix with each subsequent string and shorten it until it matches.
      Stop early if the prefix becomes empty.

Complexity:
      Time Complexity: O(n × m)
      (n = number of strings, m = length of the prefix)
      Space Complexity: O(1)

Program:
class Solution:
    def longestCommonPrefix(self,strs):
        if not strs:
            return ""
        prefix=strs[0]
        for word in strs:
            while not word.startswith(prefix):
                prefix=prefix[:-1]
                if not prefix:
                    return ""
        return prefix
