class Solution:
    def __init__(self):
        self.mod = 10**9+7
    def myPow(self, x: float, n: int) -> float:
        
        if n>0:
            if n <= 1:
                return x
            elif n%2 == 0:
                return (self.myPow(x,n//2)**2)
            else:
                return (self.myPow(x,n//2)**2)*x
        elif n < 0:
            if abs(n) <= 1:
                return 1/x
            elif n%2 == 0:
                return (self.myPow(x,n//2)**2)
            else:
                return ((self.myPow(x,n//2)**2)*(x))
        else:
            return 1

        