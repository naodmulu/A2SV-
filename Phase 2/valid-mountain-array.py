class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        if arr[0] > arr[1]:
            return False
        i = 0
        dec = False
        while i < len(arr)-1:
            if arr[i] == arr[i+1]:
                return False
            if dec and arr[i] < arr[i+1]:
                return False
            elif not dec and arr[i] > arr[i+1]:
                dec = True
            i+=1
        
        if not dec:
            return False
        return True
             


        



        