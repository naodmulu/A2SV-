class Solution:
    def numberOfWays(self, s: str) -> int:
        zeros = s.count("0")
        ones = len(s)-zeros
        
        if s[0] == "1":
            running_ones = 1
            running_zeros = 0
            ones -= 1
        else:
            running_ones = 0
            running_zeros = 1
            zeros -= 1
        count = 0
        for i in range(1,len(s)):
            if s[i] == "1":
                ones -= 1
                running_ones += 1
                if running_zeros:
                    count += zeros*running_zeros
                    
            else:
                zeros -= 1
                running_zeros += 1
                if running_ones:
                    count += ones*running_ones
            # print(running_zeros,running_ones)
        
        return count

