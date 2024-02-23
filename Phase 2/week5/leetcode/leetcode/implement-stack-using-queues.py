class MyStack:

    def __init__(self):
        self.que = deque()
        self.length = 0

    def push(self, x: int) -> None:
        self.que.appendleft(x)

    def pop(self) -> int:
        temp = deque()
        for _ in range(len(self.que)-1):
            temp.appendleft(self.que.pop())
        last = self.que.pop()
        self.que = temp
        
        return last
        

    def top(self) -> int:
        return self.que[0]
        

    def empty(self) -> bool:
        return False if self.que else True
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()