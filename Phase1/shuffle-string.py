class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        answer = ["" for n in range(len(indices))]
        for i,pos in enumerate(indices):
            
            answer[pos] = s[i]

        return "".join(answer)
        