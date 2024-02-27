class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        count = 0

        for i in range(len(height)):
            while stack and stack[-1][1] <= height[i]:
                index,val = stack.pop()
                
                if stack:
                    count += (min(stack[-1][1], height[i]) - val)*(i-stack[-1][0] -1)
            stack.append((i,height[i]))
        
        return count

        