class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = nums[:]
        self.total = 0
        for i in range(len(nums)):
            self.total += nums[i]
            self.prefix[i] = self.total
        print(self.prefix)

    def sumRange(self, left: int, right: int) -> int:
        if left:
            
            return self.prefix[right] - self.prefix[left -1]
        else:
            return self.prefix[right] 
        

        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)