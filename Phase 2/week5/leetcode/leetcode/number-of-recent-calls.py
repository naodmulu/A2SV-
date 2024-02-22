class RecentCounter:

    def __init__(self):
        self.que = deque()
        

    def ping(self, t: int) -> int:
        temp = t-3000
        if self.que:
            while self.que and self.que[-1] < temp:
                self.que.pop()
        self.que.appendleft(t)
        return len(self.que)
# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)