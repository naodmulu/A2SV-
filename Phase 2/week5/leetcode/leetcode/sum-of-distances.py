class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        check = {}
        ans = [0 for _ in range(len(nums))]
        # forward
        for i in range(len(nums)):
            if nums[i] not in check:
                check[nums[i]] = [0,i,1]
            else:
                val,index,count = check[nums[i]]
                val += abs(index - i)*count
                check[nums[i]] = [val,i,count+1]
                ans[i] += val
        # backward
        check.clear()
        for i in range(len(nums)-1,-1,-1):
            if nums[i] not in check:
                check[nums[i]] = [0,i,1]
            else:
                val,index,count = check[nums[i]]
                val += abs(index - i)*count
                check[nums[i]] = [val,i,count+1]
                ans[i] += val

        return ans
        