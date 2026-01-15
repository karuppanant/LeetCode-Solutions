Problem Number : 2273
Problem Name : Find Resultant Array After Removing Anagrams
LeetCode Link : https://leetcode.com/problems/find-resultant-array-after-removing-anagrams/submissions/1800414495/?envType=problem-list-v2&envId=array

Approach:
    Adjacent Anagram Comparison Using Sorting
    We process the words from left to right and build the result list.
    Maintain a result list
    For each word in words:
    If result is not empty and the sorted characters of the current word are equal to the sorted characters of the last word in result, it is an anagram → skip it
    Otherwise, append the word to result
    Only adjacent anagrams are removed as per the problem statement
    Sorting characters provides a canonical form to easily detect anagrams.

Complexity:
    Time Complexity: O(n × m log m)
                     where n = number of words, m = average word length
    Space Complexity: O(n) for the result list

Program:
class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        result=[]
        for word in words:
            if result and sorted(result[-1]) == sorted(word):
                continue
            result.append(word)
        return result
