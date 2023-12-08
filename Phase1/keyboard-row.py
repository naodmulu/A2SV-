class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        
        row1 = {n for n in "qwertyuiop"}
        row2 = {char for char in "asdfghjkl"}
        row3 = {char for char in "zxcvbnm"}
        
        answer = []
        temp = None
        for word in words:
            temp = set(word.lower())
            print(temp)
            if temp <= row1 or temp <= row2 or temp <= row3:
                answer.append(word)
        
        return answer
