class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        
        count = {10:0,5:0}
        for bill in bills:
            if bill == 20:
                if count[10] and count[5]:
                    count[10] -= 1
                    count[5] -= 1
                elif count[5] > 2:
                    count[5] -= 3
                else:
                    return False
            elif bill == 10:
                count[10] += 1
                if not count[5]:
                    return False
                count[5] -= 1
            else:
                count[5] += 1
        return True 
