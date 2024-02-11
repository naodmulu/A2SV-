class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        def atmost(nums, k):
            count = 0
            l = 0
            occur = {}
            ans = 0
            for r in range(len(nums)):
                if nums[r] not in occur:
                    count += 1
                    occur[nums[r]] = 1
                else:
                    occur[nums[r]] += 1

                while count > k:
                    if occur[nums[l]] == 1:
                        count -= 1
                        occur.pop(nums[l])
                    else:
                        occur[nums[l]] -= 1
                    l += 1

                ans += r-l+1

            return ans
        k = len(set(nums))
        return atmost(nums,k) -atmost(nums,k-1)
                

            
