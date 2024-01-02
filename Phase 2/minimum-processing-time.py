class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort()
        tasks.sort(reverse = True)
        ans = -1
        for i in range(len(processorTime)):
            temp = 0
            for j in range(4):
                val = (4*i) + j
                # print(val,processorTime[i] + tasks[val])
                temp = max(temp,processorTime[i] + tasks[val])
            # print(temp)
            ans = max(ans,temp)
        
        return ans
        # time complexity = O(nlogn)
        # space = O(1)