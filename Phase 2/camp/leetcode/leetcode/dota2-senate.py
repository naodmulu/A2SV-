class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        que = deque(i for i in senate)
        r_count = senate.count("R")
        d_count = len(senate)-r_count
        d ,r = 0,0
        while d_count and r_count:
            cur = que.popleft()
            if cur == "R":
                if d == 0:
                    r += 1
                    que.append(cur)
                else:
                    d -= 1
                    r_count -= 1
            else:
                if r == 0:
                    d += 1
                    que.append(cur)
                else:
                    r -= 1
                    d_count -= 1
                    
        return "Radiant" if r_count else "Dire"