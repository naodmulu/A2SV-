class OrderedStream:

    def __init__(self, n: int):
        self.place = [0]*n
        self.pointer = 0
        self.n = n

        

    def insert(self, idKey: int, value: str) -> List[str]:
        pos = idKey - 1
        self.place[pos] = value
        temp = []
        while self.pointer < self.n:
            if self.place[self.pointer]:
                temp.append(self.place[self.pointer]) 
                self.pointer += 1
            elif self.place[self.pointer] == 0 or pointer >= self.n:
                break
        
        return temp


        
        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)