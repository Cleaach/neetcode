class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        nums.sort(reverse=True)
        self.arr = []
        for i in range(min(len(nums),k)):
            self.arr.append(nums[i])
        heapq.heapify(self.arr)
        self.k = k

    def add(self, val: int) -> int:
        heapq.heappush(self.arr, val)
        if len(self.arr) > self.k:
            heapq.heappop(self.arr)
        return self.arr[0]
