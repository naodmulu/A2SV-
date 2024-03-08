class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:

        remaining = sum(nums) % p
        if remaining == 0:
            return 0
        
        prefix = [0]
        for num in nums:
            prefix.append((prefix[-1] + num) % p)
        # print(prefix)

        ans = len(nums)
        count = {}
        for idx, r in enumerate(prefix):
            if (r -remaining)%p in count:
                ans = min(ans,idx- count[(r - remaining)%p])
            
            count[r] = idx

        if ans == len(nums):
            return -1
        return ans

        