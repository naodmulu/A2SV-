class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        def helper(n):
            print(n)
            if n == 1:
                print("yes")
                return True
            elif n < 3:
                return False
            else:
                return helper(n/3)
        return helper(n)
        