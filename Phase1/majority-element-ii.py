
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        target = len(nums)//3
        counter = {}
        answer = []
        for num in nums:
            counter[num] = counter.get(num, 0) + 1 

        for key,value in counter.items():
            if value > target:
                answer.append(key)

        return answer