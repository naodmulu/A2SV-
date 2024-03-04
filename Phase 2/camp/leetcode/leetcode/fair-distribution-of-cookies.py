class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        self.mini = float("inf")
        self.buckets = [0 for _ in range(k)]
        cookies.sort(reverse = True)

        def helper(idx):
            if idx >= len(cookies):
                self.mini = min(self.mini,max(self.buckets))
                return

            for i in range(k):
                if self.buckets[i] + cookies[idx] <= self.mini:
                    self.buckets[i] += cookies[idx]
                    helper(idx+1)
                    self.buckets[i] -= cookies[idx]
        helper(0)
        return self.mini
        