class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda x:x[2],reverse = True)
        prefix = [0 for _ in range(trips[0][2]+1)]
        for ppl,start,end in trips:
            prefix[start] += ppl
            prefix[end] -= ppl
        
        total = 0
        for i in range(len(prefix)):
            total += prefix[i]
            if total > capacity:
                return False
            prefix[i] = total
        # print(prefix)
        return True


        