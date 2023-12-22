class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        ans = [bits[::-1] for bits in image ]

        for i in range(len(ans)):
            for j in range(len(ans)):
                ans[i][j] = 1 - ans[i][j] 
        return ans