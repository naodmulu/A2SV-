class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
    
        count = 0
        curr = int()
        flip_value = int()
        

        for i in range(1,len(flips)+1):
            curr += i
            flip_value += flips[i-1]

            if curr == flip_value:
                count += 1

        return count 
        
                