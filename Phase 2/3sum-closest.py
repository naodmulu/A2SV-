class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        print(nums)
        ans = []
        for i in range(len(nums)-2):
            
            j = i+1
            k = len(nums) -1
            while j < k:
                if nums[i] + nums[j]+nums[k] > target:
                    ans.append(nums[i] + nums[j]+nums[k])
                    k -= 1
                elif nums[i] + nums[j]+nums[k] < target:
                    ans.append(nums[i] + nums[j]+nums[k])
                    j += 1
                else:
                    return nums[k]+nums[i]+nums[j]
        ans.sort(key=lambda x:abs(x-target))
        return ans[0]

            

        
        