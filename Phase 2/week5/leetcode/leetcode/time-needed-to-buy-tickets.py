class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        que = deque()
        t= 0
        for i in range(len(tickets)):
            que.append([tickets[i],i])
            t += tickets[i]
        ans = 0
        # print(que,t)
        i = 0
        count = 0
        while i <= t and que:
            count += 1
            temp_val,temp_index = que.popleft()
            if temp_index == k and temp_val == 1:
                return count
            if temp_val != 1:
                que.append([temp_val -1, temp_index])
            
