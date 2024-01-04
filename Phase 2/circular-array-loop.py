class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        
        for i in range(len(nums)):
            walk = i
            occur = set()
            if nums[i] > 0:
                postive = True
            elif nums[i] < 0:
                postive = False
            else:
                continue

            while 1:
                # print(walk)
                if postive:
                    if nums[walk] < 0:
                        break
                else:
                    if nums[walk] > 0:
                        break 
                if walk not in occur:
                    occur.add(walk)
                else:
                    if len(occur) == 1:
                        break
                    elif len(occur) > 1 and walk == i:
                        return True
                    else:
                        break
                # print("new",nums[walk]%len(nums))
                walk += nums[walk]
                walk = walk%len(nums)
                # print(occur)
                
        return False
                



        