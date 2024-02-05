class Solution:
    def minimumSteps(self, s: str) -> int:
        if len(s) == 1:
            return 0
        # seek,pos,ans = 0,0,0
        # check = [n for n in s]
        # while pos < len(s) and seek < len(s):
        #     if check[pos] == "0":
        #         pos += 1
        #     elif check[pos] == "1":
        #         seek = pos
        #         while seek < len(s):
        #             if check[seek] == "0":
        #                 ans += seek - pos
        #                 check[pos],check[seek] = check[seek],check[pos]
        #                 pos = seek
        #                 break
        #             seek += 1
        # return ans
        count,ans = 0,0
        for i in range(len(s)-1,-1,-1):
            if s[i] == "0":
                count += 1
            else:
                ans += count
        return ans

