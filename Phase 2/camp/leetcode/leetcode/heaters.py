class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        def checker(val):
            he = 0
            ho = 0
            while ho < len(houses) and he < len(heaters) :
                # print(heaters[he]-houses[ho],val)
                if abs(heaters[he] - houses[ho]) <= val:
                    ho += 1
                else:
                    he += 1
            print(ho == len(houses),he <len(heaters))
            return ho == len(houses)
                
        l = 0
        r = max(abs(houses[-1]-heaters[0]),abs(houses[0]-heaters[-1]))
        ans = r
        while l <= r:
            mid = (l+r)//2
            # print(l,r)
            # print(mid)
            if checker(mid):
                ans = mid
                r = mid -1
            else:
                l = mid +1 

        return ans