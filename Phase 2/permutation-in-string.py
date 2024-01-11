class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        target = Counter(s1)
        l = 0
        r = len(s1) -1
        window = {}
        for i in range(len(s1)):
            if s2[i] in window:
                window[s2[i]] += 1
            else:
                window[s2[i]] = 1

        if window == target:
            return True
        while l < len(s2)- len(s1) and r < len(s2):
            r += 1
            if s2[r] in window:
                window[s2[r]] += 1
            else:
                window[s2[r]] = 1
            window[s2[l]] -= 1
            if window[s2[l]] <= 0:
                del window[s2[l]]
            if window == target:
                return True
            l += 1

        return False


        