class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        dic = Counter(arr)
        target = len(arr)*0.25
        print (target)
        for key,value in dic.items():
            if value > target:
                return key

        
        