class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0 for _ in range(len(temperatures))]
        for t in range(len(temperatures)):
            while stack and stack[-1][1] < temperatures[t]:
                index,val = stack.pop()
                ans[index] = t - index
            stack.append((t,temperatures[t]))
        return ans 

        