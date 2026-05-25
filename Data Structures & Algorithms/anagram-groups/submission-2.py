from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for word in strs:
            arr = [0] * 26
            for char in word:
                arr[ord(char) - ord('a')] += 1
            key = tuple(arr)  
            anagrams[key].append(word)
        return list(anagrams.values())
