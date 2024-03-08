class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        def helper(k,n):
            if n == 1:
                return 0
            
            val = helper((k+1)//2,n-1)
            
            if val == 0:
                if k%2 ==1:
                    return 0
                else:
                    return 1
            
            else:
                if k%2 == 0:
                    return 0
                else:
                    return 1


            # if n == 2:
            #     if k == 1:
            #         return 0
            #     return 1
            # # print(k)
            # mid = pow(2,n-1)
            # if k > mid:
            #     k -= mid
            #     return 1 - helper(ceil(k/mid),n-1)
            # else:
            #     return helper(ceil(k/mid),n-1)
        
        return helper(k,n)


        