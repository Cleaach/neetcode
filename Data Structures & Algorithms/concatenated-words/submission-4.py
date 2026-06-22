class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        wordset = set(words)
        memo = {}
    
        def help(word):
            if word in memo:
                return memo[word]
            
            # split the word at all indices
            for i in range(1, len(word)):
                pre = word[:i]
                post = word[i:]

                if pre in wordset:
                    if post in wordset or help(post):
                        memo[word] = True
                        return True
            
            memo[word] = False
            return False
        
        res = []
        for a in words:
            if help(a):
                res.append(a)
        
        return res
        
            
        