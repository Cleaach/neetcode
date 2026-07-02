class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        h = [] # (freq, element)
        heapq.heapify_max(h)
        q = deque() # (freq, time ready, element)

        # insert ints to heap
        c = Counter(tasks)
        for key, value in c.items():
            heapq.heappush_max(h, (value, key))
        
        time = 0
        while h or q:
            if q and q[0][1] == time:
                new = q.popleft()
                heapq.heappush_max(h, (new[0], new[2]))
            
            if not h:
                time += 1
                continue

            most = heapq.heappop_max(h)
            time += 1
            if most[0] > 1:
                q.append((most[0] - 1, n + time, most[1]))
        
        return time
                

            