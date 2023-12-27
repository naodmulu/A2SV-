class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        minn = min(nums)
        maxx = max(nums)
        sorted_nums = [0 for _ in range(maxx- minn+1)]
        
        for num in nums:
            sorted_nums[num-minn] += 1
        print(sorted_nums)
        nums_s = []
        for i in range(len(sorted_nums)):
            if sorted_nums[i] > 0:
                for j in range(sorted_nums[i]):
                    nums_s.append(i+minn)
        print(nums_s)
        return [i for i in range(len(nums_s)) if nums_s[i] == target]



        