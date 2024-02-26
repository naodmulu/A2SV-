class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        temp = self.fib(n-1) + self.fib(n-2)
        return temp

        