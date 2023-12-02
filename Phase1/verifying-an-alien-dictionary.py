class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        alienorder = {}
        for i, char in enumerate(order):
            alienorder[char] = i
        print(alienorder)
        def comparetwowords(word1, word2):
            for i in range(min(len(word1), len(word2))): 
                char1 = word1[i]
                char2 = word2[i]  
                if alienorder[char1] < alienorder[char2]:
                    return True
                elif alienorder[char1] > alienorder[char2]:
                    return False
            return len(word1) <= len(word2)
    
        for i in range(len(words) - 1):
            if not comparetwowords(words[i], words[i + 1]):
                return False
        return True