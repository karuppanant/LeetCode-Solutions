Problem Number : 2402
Problem Name : Meeting Rooms III
LeetCode Link : https://leetcode.com/problems/meeting-rooms-iii/submissions/1866761737/?envType=problem-list-v2&envId=array

Approach:
      Min-Heap for Free and Busy Rooms (Greedy + Priority Queue)
      Sort meetings by start time.
      Maintain:
      free_room → min-heap of available room numbers
      busy_room → min-heap of (end_time, room) for ongoing meetings
      count → number of meetings held per room
      For each meeting (start, end):
      Release rooms from busy_room whose end_time <= start and push them to free_room.
      If a free room exists:
      Assign meeting to the smallest numbered free room.
      If no free room:
      Take the earliest ending busy room, delay meeting to start after current end, and push back into busy_room.
      Update meeting count for assigned room.
      Return the room with maximum meetings held.

Complexity:
      Time Complexity: O(m log n)
                       where m = number of meetings, n = number of rooms
      Space Complexity: O(n)

Program:
import heapq
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        free_room=list(range(n))
        heapq.heapify(free_room)
        busy_room=[]
        count=[0]*n
        for start,end in meetings:
            duration=end-start
            while busy_room and busy_room[0][0]<=start:
                _,room=heapq.heappop(busy_room)
                heapq.heappush(free_room,room)
            if free_room:
                room=heapq.heappop(free_room)
                heapq.heappush(busy_room,(end,room))
            else:
                end_time,room=heapq.heappop(busy_room)
                heapq.heappush(busy_room,(end_time+duration,room))
            count[room]+=1
        return count.index(max(count))
