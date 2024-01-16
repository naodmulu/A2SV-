class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def atmost(nums, k):
            count = 0
            l = 0
            ans = 0
            for r in range(len(nums)):
                if nums[r]%2:
                    count += 1

                while count > k:
                    if nums[l]%2:
                        count -= 1
                    l += 1

                ans += r-l+1

            return ans

        return atmost(nums,k) -atmost(nums,k-1)
                

            

