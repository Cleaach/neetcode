class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones) # heappop_max removes heaviest
        while len(stones) > 1:
            first = heapq.heappop_max(stones)
            second = heapq.heappop_max(stones)
            if first == second:
                continue
            else:
                heapq.heappush_max(stones, first - second)
        if len(stones) == 1:
            return stones[0]
        else:
            return 0
