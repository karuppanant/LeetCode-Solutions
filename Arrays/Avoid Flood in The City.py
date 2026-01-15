Problem Number : 1488
Problem Name : Avoid Flood in The City
LeetCode Link : https://leetcode.com/problems/avoid-flood-in-the-city/submissions/1794431854/?envType=problem-list-v2&envId=array

Approach:
Greedy + HashMap + Sorted Structure
Each lake must be dried after its previous rain and before it rains again.

Use:
last_rain_day → stores last day a lake was filled.
dry_day (SortedList) → stores indices of available dry days (rains[i] == 0).
ans → result array.

Logic:
Traverse each day i:
If rains[i] > 0:
Mark ans[i] = -1 (rain day).
If lake was filled before:
Find the earliest dry day after last rain using bisect_right.
If none exists → flood → return [].
Assign that dry day to dry this lake.
Update last_rain_day.
If rains[i] == 0:
Store this index as a potential dry day.
Temporarily set ans[i] = 1 (default dry action).
Return ans if successful.

Why SortedList?
To efficiently find the next valid dry day (O(log n)).
Python fallback is implemented using bisect if sortedcontainers is unavailable.

Complexity:
Time Complexity: O(n log n)
Space Complexity: O(n)

Program:
import collections
try:
    from soretedcontainers import SortedList
except:
    ImportError
    
    class SortedList(list):
        def add(self,val):
            import bisect
            bisect.insort_left(self,val)
        def bisect_right(self,val):
            return bisect.bisect_right(self,val)
        def pop(self,index):
            return super().pop(index)
class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        n=len(rains)
        ans=[1]*n
        last_rain_day={}
        dry_day=SortedList()
        for i in range(n):
            lake_id=rains[i]

            if lake_id>0:
                ans[i]=-1

                if lake_id in last_rain_day:
                    s=dry_day.bisect_right(last_rain_day[lake_id])

                    if s==len(dry_day):
                        return []

                    j=dry_day.pop(s)
                    ans[j]=lake_id

                last_rain_day[lake_id]=i

            else:
                dry_day.add(i)
                ans[i]=1
        
        return ans
