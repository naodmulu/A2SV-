class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        mini = []
        temp = float("inf")
        for i in range(len(nums)):
            mini.append(temp)
            temp = min(temp,nums[i])
        for i in range(len(nums)-1,-1,-1):
            while stack and stack[-1] < nums[i]:
                if stack.pop() > mini[i]:
                    return True
            stack.append(nums[i])

        return False
        