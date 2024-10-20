"""
Python Data Structures - A Game-Based Approach
Priority Queue Class based on heapq.
Robin Andrews - https://compucademy.net/
"""

import heapq


class PriorityQueue:
    def __init__(self) -> None:
        self.elements = []
    def is_empty(self):
        return not self.elements
    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))
    def get(self):
        return heapq.heappop(self.elements)[1]
    def __str__(self) -> str:
        return str(self.elements)
    
if __name__ == "__main__":
    pq = PriorityQueue()
    pq.put("chill", 2)
    pq.put("work", 1)
    pq.put("sleep", 3)
    print(pq)
    print(pq.get())
    print(pq.get())
    print(pq.get())

