class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:

        answer = ""
        answer += s[:spaces[0]]

        for i in range(len(spaces)-1):
            answer += " " + s[spaces[i]:spaces[i+1]]
    
        return answer + " " + s[spaces[-1]:]


        