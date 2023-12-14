class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        same_value = set()
        length = len(fronts)
        smallest = 0
        for i in range(length):
            if fronts[i] == backs[i]:
                same_value.add(fronts[i])

        for i in range(length):
            if fronts[i] not in same_value:
                if smallest:
                    smallest = min(smallest,fronts[i])
                else:
                    smallest = fronts[i]
            if backs[i] not in same_value:
                if smallest:
                    smallest = min(smallest,backs[i]) 
                else:
                    smallest = backs[i]
        
        return smallest
        # time = O(n)
        # space = O(n)
        