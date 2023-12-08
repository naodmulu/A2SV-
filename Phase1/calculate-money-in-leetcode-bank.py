class Solution:
    def totalMoney(self, n: int) -> int:
    
        total = 0
        weeks = n // 7  
        
        for i in range(weeks):

            total += 28 + 7 * i  
        
        remainder = n % 7  
        
        for i in range(1, remainder + 1):
            total += (weeks + 1) + i - 1  

        return total
