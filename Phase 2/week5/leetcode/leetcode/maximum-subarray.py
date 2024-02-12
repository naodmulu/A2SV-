class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total = 0
        # prefix = [0]
        # for i in range(len(nums)):
        #     total += nums[i]
        #     prefix.append(total)
        # print(prefix)
        # ans = (-1*(10**4)) - 1
        # for l in range(len(prefix)-1):
        #     r = l+1
        #     while r < len(prefix):
        #         ans = max(ans,prefix[r]-prefix[l])
        #         r += 1
        l = 0
        ans = (-1*(10**4)) - 1
        for r in range(len(nums)):
            total += nums[r]
            ans = max(ans,total)
            while total < 0:
                total -= nums[l]
                l +=1

        return ans

        