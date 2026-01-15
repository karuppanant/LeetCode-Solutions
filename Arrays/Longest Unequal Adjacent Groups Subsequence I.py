Problem Number : 2686
Problem Name : Maximum Subsequence of Words With Distinct Letters
LeetCode Link : https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-i/submissions/1776110489/?envType=problem-list-v2&envId=array

Approach:
      Greedy Subsequence Selection
      Initialize result with the first word.
      Traverse the words from index 1 to end:
      If the current group differs from the previous group, append the word to result.
      Return the result list.
      This ensures that no two consecutive words in the result belong to the same group.

Complexity:
      Time Complexity: O(n)
                       where n = number of words
      Space Complexity: O(n)

Program:
class Solution:
    def getLongestSubsequence(self, words, groups):
        result=[words[0]]
        for i in range(1,len(words)):
            if groups[i]!=groups[i-1]:
                result.append(words[i])
        return result
