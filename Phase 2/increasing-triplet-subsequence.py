class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 2:
            return False
        i = 2**31
        j = 2**31

        for k in range(len(nums)):
            if nums[k] <= i:
                i = nums[k]
            elif nums[k] <= j:
                j = nums[k]
            elif nums[k] > i and nums[k] > j:
                return True
        
        return False
            
        

            
          
            
                
