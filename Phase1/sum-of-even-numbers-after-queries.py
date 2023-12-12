class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        ans= []
        summ = 0
        
        for i in range(len(nums)):
            if nums[i]%2 == 0:
                summ += nums[i]
        
        for val,index in queries:
            if nums[index]%2 == 0 and val%2 == 1:
                summ -= nums[index]
                nums[index] += val
                ans.append(summ)
            elif nums[index]%2 == 0 and val%2 == 0:
                summ +=  val
                nums[index] += val
                ans.append(summ)
            elif nums[index]%2 == 1 and val%2 == 0:
                nums[index] += val
                ans.append(summ)
            elif nums[index]%2 == 1 and val%2 == 1:
                summ += nums[index] + val
                nums[index] += val
                ans.append(summ)

        if not ans:
            ans.append(0) 
        return ans
        