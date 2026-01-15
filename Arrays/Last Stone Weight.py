Problem Number : 1046
Problem Name : Last Stone Weight
LeetCode Link : https://leetcode.com/problems/last-stone-weight/submissions/1797360001/?envType=problem-list-v2&envId=array

Approach:
    Max Heap (Priority Queue) Approach
    Use a max heap to always extract the two heaviest stones.
    Smash the two stones; if they are not equal, insert the remaining weight back into the heap.
    Repeat until at most one stone remains.

Complexity:
    Time Complexity: O(n log n)
    Space Complexity: O(n)

Program:
import heapq
class Solution:
    def lastStoneWeight(self,stones):
        max_heap=[]
        for stone in stones:
            heapq.heappush(max_heap,-stone)
        while len(max_heap)>1:
            y=-heapq.heappop(max_heap)
            x=-heapq.heappop(max_heap)

            if y!=x:
                new_stone_weight=y-x
                heapq.heappush(max_heap,-new_stone_weight)

        if not max_heap:
            return 0
        else:
            return -heapq.heappop(max_heap)
        
