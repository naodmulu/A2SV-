class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        que = deque()
        
        ans = []
        for i in range(k):
            
            while que and que[-1] < nums[i]:
                que.pop()
            que.append(nums[i])
        ans.append(que[0])            
        r = k
        l = 0
        while r < len(nums):
            if nums[l] == que[0]:
                que.popleft()
            while que and que[-1] < nums[r]:
                que.pop()
            que.append(nums[r])
            ans.append(que[0])
            l += 1
            r += 1
                      
        return ans