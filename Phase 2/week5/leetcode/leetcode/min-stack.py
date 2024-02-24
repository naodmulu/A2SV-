class MinStack:

    def __init__(self):
        self.stack = []
        self.mini = float("inf")

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.mini = min(self.mini,val)

    def pop(self) -> None:
        temp = self.stack.pop()
        if self.mini == temp:
            if self.stack:
                self.mini = min(self.stack)
            else:
                self.mini = float("inf")      

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.mini
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()