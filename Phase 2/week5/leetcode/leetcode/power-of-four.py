class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        def four(n):
            if n == 1:
                return 1
            if n < 4:
                return False
            return four(n/4)
        return four(n)
        