class Solution:
    def freqAlphabets(self, s: str) -> str:
        l= len(s) - 1
        ans =[]
        order = {}
        i = 1
        for char in string.ascii_lowercase:
            order[i] = char
            i +=1
        # print(order)
        while l >= 0:
            if s[l] == "#":
                temp = s[l-2] + s[l-1]
                ans.append(order[int(temp)])
                l -=3
            else:
                temp = s[l]
                ans.append(order[int(temp)])
                l-=1
        return "".join(ans[::-1])