class Solution:
    def isHappy(self, n: int) -> bool:
        
        tset = set()
        def check (n):
            if  n in tset:
                return False
            tset.add(n)
            temp = [int(n)**2 for n in str(n)]
            summ = sum(temp)
            
            if summ == 1:
                return True
            else:
               return check(summ)
        return check(n)

            
        