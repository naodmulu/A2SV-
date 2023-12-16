class Bitset:

    def __init__(self, size: int):
        self.size = size
        self.arr = [0] *size
        self.ones = 0
        self.flipped = False
        

    def fix(self, idx: int) -> None:
        if not self.flipped:
            if not self.arr[idx]:
                self.arr[idx] = 1
                self.ones += 1
        else:
            if self.arr[idx]:
                self.arr[idx] = 0
                self.ones -= 1
        

    def unfix(self, idx: int) -> None:
        if self.flipped:
            if not self.arr[idx]:
                self.arr[idx] = 1
                self.ones += 1
        else:
            if self.arr[idx]:
                self.arr[idx] = 0
                self.ones -= 1
        

    def flip(self) -> None:
        self.flipped = not self.flipped  

    def all(self) -> bool:
        if self.flipped:
            return self.ones == 0
        else:
            return self.ones == self.size

    def one(self) -> bool:
        if self.flipped:
            return self.ones != self.size
        else:
            return self.ones > 0

    def count(self) -> int:
        if self.flipped:
            return self.size - self.ones
        else:
            return self.ones

    def toString(self) -> str:
        if self.flipped:
            s = []
            for i in self.arr:
                if i == 0:
                    s.append("1")
                else:
                    s.append("0")
            return "".join(s)

        return "".join(str(bit) for bit in self.arr )

#time complexity = O(n)
#space = O(n)
   
        


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()