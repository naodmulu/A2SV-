import random
class RandomizedSet:

    def __init__(self):
        self.index = {}
        self.value = []
        self.length = 0
        
        

    def insert(self, val: int) -> bool:
        if val in self.index:
            return False
        else:
            self.value.append(val)
            self.index[val] = self.length
            self.length += 1
            return True

    def remove(self, val: int) -> bool:
        if val in self.index:
            temp_index = self.index[val] 
            last_val = self.value[-1]
            self.value[temp_index] = last_val
            self.index[last_val] = temp_index
            self.value.pop()
            self.length -= 1

            del self.index[val]
            return True
        else:
            return False
        

    def getRandom(self) -> int:
        i = random.randint(0,self.length - 1)
        return self.value[i]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()