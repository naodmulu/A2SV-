class ATM:

    def __init__(self):
        self.current_notes = [0,0,0,0,0]
        self.notes = [20,50,100,200,500]
        

    def deposit(self, banknotesCount: List[int]) -> None:
        for i in range(5):
           self.current_notes[i] += banknotesCount[i]
        

    def withdraw(self, amount: int) -> List[int]:
        withdrawn = [0,0,0,0,0]
        i = 4

        while i >= 0:
            amount_av = amount // self.notes[i]
            # print(amount_av)
            withdrawn[i] = min(amount_av,self.current_notes[i])
            # print(withdrawn[i])
            amount -= self.notes[i] * withdrawn[i]
            # print(i)
            i -=1

        if amount > 0:
            return [-1]
        else:
            for i in range(5):
                self.current_notes[i] -= withdrawn[i]

        return withdrawn

# time complexity = O(1)
# space = O(1)

# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)