class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        postive = []
        negative = []
        answer = []
        for num in nums:
            if num > 0:
                postive.append(num)
            else:
                negative.append(num)

        for i in range(len(postive)):
            answer.append(postive[i])
            answer.append(negative[i])
        
        return answer








