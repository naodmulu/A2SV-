class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        arr = nums.copy()*2
        for i in range(len(arr)):
            # print(stack)
            temp = arr[i]
            arr[i] = -1
            while stack and stack[-1][1] < temp:
                index,val = stack.pop()
                arr[index] = temp
            stack.append((i,temp))
        return arr[:len(nums)]
        