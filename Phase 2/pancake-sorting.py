class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        ans = []
        for i in range(len(arr),0,-1):
            segement = []
            maxIndex = arr.index(i)
            if maxIndex == 0:
                segement = arr[i-1::-1] + segement[i:]
                arr = segement
                ans.append(i)
                
            elif maxIndex == i-1:
                continue
            else:
                segement = arr[maxIndex::-1] + arr[maxIndex+1:]
                ans.append(maxIndex+1)
                segement = segement[i-1::-1] + segement[i:]
                arr = segement
                ans.append(i)


        
        return ans
            




        