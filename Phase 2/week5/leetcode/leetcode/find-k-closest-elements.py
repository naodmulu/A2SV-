class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        indx = 0
        for i in range(len(arr)):
            if abs(arr[indx] - x) < abs(arr[i] -x) or (abs(arr[indx] - x) == abs(arr[i] - x) and arr[indx] < arr[i]):
                continue
            else:
                indx = i

        l = r = indx
        while r-l+1 != k:
            if l == 0 and r == len(arr)-1:
                break
            if l == 0:
                r += 1
            elif r == len(arr)-1:
                l -= 1
            else:
                templ = l-1
                tempr = r +1
                if abs(arr[templ] - x) < abs(arr[tempr] -x) or (abs(arr[templ] - x) == abs(arr[tempr] - x) and arr[templ] < arr[tempr]):
                    l -= 1
                else:
                    r += 1
                    
                
        return arr[l:r+1]