class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        mod = (10**9)+7
        maxx = 0
        
        minn = float("inf")
        for start,end in requests:
            maxx = max(maxx,end)
            minn = min(minn,start)
        print(maxx,minn)
        prefix = [0 for _ in range(maxx-minn+2)]
        for start,end in requests:
            prefix[start-minn] += 1
            prefix[end-minn+1] -= 1
        total = 0
        for i in range(len(prefix)):
            total += prefix[i]
            prefix[i] = total
        prefix.pop()
        prefix.sort(reverse=True)
        nums.sort(reverse=True)
        ans = 0
        for i in range(len(prefix)):
            ans += nums[i]*prefix[i]
        print(prefix)
        return ans%mod

        