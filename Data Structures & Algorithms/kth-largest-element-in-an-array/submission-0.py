class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        arr = []
        heapq.heapify_max(arr)
        for num in nums:
            heapq.heappush_max(arr, num)
        for i in range(k):
            res = heapq.heappop_max(arr)
        return res