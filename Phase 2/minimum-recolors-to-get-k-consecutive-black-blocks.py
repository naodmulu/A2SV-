class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l = 0
        r = k-1
        count = 0
        for i in range(k):
            if blocks[i] == "W":
                count += 1
        temp = count
        while l < len(blocks)-k and r < len(blocks):
            r += 1
            if blocks[r] == "W":
                temp += 1
            if blocks[l] == "W":
                temp -= 1
            l += 1
            count = min(count,temp)
        return count
        