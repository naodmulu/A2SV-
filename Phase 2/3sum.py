class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        print(nums)
        if nums[0] > 0:
            return []
        ans = set()
        j = len(nums) -1
        for k in range(len(nums)-2):
            
            i = k+1
            j = len(nums) -1
            while i < j:
                if nums[i] + nums[j]+nums[k] > 0:
                    j -= 1
                elif nums[i] + nums[j]+nums[k] < 0:
                    i += 1
                else:
                    ans.add((nums[k],nums[i],nums[j]))
                    i += 1
                    j -= 1
        return ans

            

        