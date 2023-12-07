class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        totalset = set()
        for i in ranges:
            totalset.update(set(range(i[0],i[1]+1)))
        print(totalset)
        for v in range(left,right+1):
            if v not in totalset:

                return False
        
        return True
