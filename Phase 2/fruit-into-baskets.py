class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l = 0
        count = defaultdict(int)
        temp = 0
        ans = 0
        for r in range(len(fruits)):
            count[fruits[r]] += 1          
            temp += 1
            while len(count) > 2:
                # print(l)
                count[fruits[l]] -= 1
                temp -= 1

                if count[fruits[l]] == 0:
                    del count[fruits[l]]
                l += 1
            
            ans = max(temp,ans)

        return ans



            

        