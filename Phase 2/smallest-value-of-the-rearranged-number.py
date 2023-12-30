class Solution:
    def smallestNumber(self, num: int) -> int:
        if num == 0:
            return 0
        num_str = str(abs(num))  
        count = {str(i): 0 for i in range(10)}  
        
        for n in num_str:
            count[n] += 1
        
        ans = ""
        pos_zero = 0  
        if num > 0:
            for i in range(1, 10):
                if count[str(i)] > 0:
                    if pos_zero == 0:
                        ans += str(i)
                        ans += str(0)*count[str(0)]
                        ans += str(i)*(count[str(i)]-1)
                        pos_zero = 1
                    else:
                        ans += str(i)*count[str(i)] 
            
            return int(ans)

        else:
            for i in range(9,-1,-1):
                if count[str(i)] > 0:
                    ans += str(i)*count[str(i)]
            ans = "-" + ans
            return int(ans)
            
        
        