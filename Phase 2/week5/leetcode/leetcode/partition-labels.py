class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        count = Counter(s)
        # print(count)
        ans = []
        temp = 0
        check = {}
        for i in range(len(s)):
            temp +=1 
            if s[i] in check:
                check[s[i]] += 1
            else:
                check[s[i]] = 1
            if all(check[key] == count[key] for key in check):
                ans.append(temp)
                temp = 0
                check.clear()
        return ans
            

        