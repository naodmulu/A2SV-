class Solution:
    def helper(self,nums,i,j,turn):
        if i > j:
            return 0
        if turn:
            return max(nums[i] + self.helper(nums,i+1,j,not turn),nums[j] + self.helper(nums,i,j-1,not turn))
        else:
            return min(-nums[i] + self.helper(nums,i+1,j,not turn),-nums[j] + self.helper(nums,i,j-1,not turn))

    def predictTheWinner(self, nums: List[int]) -> bool:
        ans = self.helper(nums,0,len(nums)-1,True)
        # print(ans)

        if ans >= 0:
            return True
        
        return False
        
        
           