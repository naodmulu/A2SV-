class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        r = 0
        count = 0
        temp = k
        while r < len(nums) and l < len(nums):
            if nums[r] == 1:
                r += 1
            elif nums[r] == 0 and temp > 0:
                r += 1
                temp -= 1
            elif not nums[r] and not temp:
                if nums[l]:
                    l += 1
                elif not nums[l]:
                    l += 1
                    temp += 1
            
            count = max(count,r-l)
        # print(len(nums))
        return count

        # time complexity = O(n)
        #space = O(1)

