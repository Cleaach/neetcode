class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        indices = set()

        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue
            if t[0] == target[0]:
                indices.add(0)
            if t[1] == target[1]:
                indices.add(1)
            if t[2] == target[2]:
                indices.add(2)
        
        return len(indices) == 3
