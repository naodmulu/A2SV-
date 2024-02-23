class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        removedBy = {}
        for num in nums2:
            # print(stack)
            while stack and stack[-1] < num:
                removedBy[stack.pop()] = num

            stack.append(num)
        for i in range(len(nums1)):
            if nums1[i] in removedBy:
                nums1[i] = removedBy[nums1[i]]
            else:
                nums1[i] = -1
        return nums1

        
        