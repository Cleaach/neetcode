class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()  # Sort to group duplicates together
        
        def backtrack(start, curr, remaining):
            # Base case: found valid combination
            if remaining == 0:
                res.append(curr[:])
                return
            
            # Base case: target exceeded
            if remaining < 0:
                return
            
            # Try each candidate from start onwards
            for i in range(start, len(candidates)):
                # Skip duplicates: if this is the same value as the previous index
                # and we didn't use the previous index, skip this one
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                
                # Choose: add candidate
                curr.append(candidates[i])
                
                # Explore: move to next index (start = i + 1, no reuse)
                backtrack(i + 1, curr, remaining - candidates[i])
                
                # Unchoose: backtrack
                curr.pop()
        
        backtrack(0, [], target)
        return res