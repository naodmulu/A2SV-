class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack = [] 
        ans = 0
        mod = 10 ** 9 + 7
        for i in range(len(arr)):
            while stack and stack[-1][1] > arr[i]:
                index, val = stack.pop()
                if stack:
                    l = index - stack[-1][0]
                else:
                    l = index +1
                r = i - index
                temp = l*r
                ans += val*temp
            stack.append((i, arr[i]))
        
        for i in range(len(stack)):
            index, val = stack[i]
            if i > 0:
                l = index - stack[i-1][0]
            else:
                l = index +1
            r = len(arr) - index
            temp = l*r
            ans += val*temp

        return ans%mod
        