class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        count = Counter(nums)
        ans = 0
        temp = 0
        for key in sorted(count.keys(), reverse = True):
            ans += temp
            temp += count[key]
        return ans