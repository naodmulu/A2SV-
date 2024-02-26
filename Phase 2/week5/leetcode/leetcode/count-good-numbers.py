class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = 10**9 + 7
        
        if n == 1:
            return 5
        def helper(n):
            if n <= 1:
                return 20
            elif n%2 == 0:
                return (helper(n//2)**2)% mod
            else:
                return ((helper(n//2)**2)*20)% mod
        return helper(n//2)%mod if n%2 == 0 else (helper((n-1)//2)*5)%mod

