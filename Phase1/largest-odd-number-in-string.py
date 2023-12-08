class Solution:
    def largestOddNumber(self, num: str) -> str:
        max_odd = -1

        nums = list(map(int,num))
        i = len(nums)-1
        if nums[i]%2 == 1:
            return num
        else:
            i -= 1
        while i >= 0:
            if nums[i]%2 == 1:
                return "".join(map(str,nums[:i+1]))
            i -= 1
        return ""


        