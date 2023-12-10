class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        position = {}
        for i in range(len(nums)):
            position[nums[i]] = i
        temp = 0
        for x,y in operations:
            temp = position[x]
            nums[temp] = y
            position[y] = temp
            
        
        return nums