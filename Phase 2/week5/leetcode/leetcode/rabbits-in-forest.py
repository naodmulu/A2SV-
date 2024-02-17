class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = Counter(answers)
        print(count)
        total = 0
        for key in count.keys():
            # print(key+1,count[key],ceil(count[key]/(key+1)))
            total += ceil(count[key]/(key+1))*(key+1)
            

        return total
        