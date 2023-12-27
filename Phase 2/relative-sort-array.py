class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        
        arr2_dic = {num:0 for num in arr2}
        not_in = []

        for num in arr1:
            if num in arr2_dic:
                arr2_dic[num] += 1
            else:    
                not_in.append(num)
        ans = []
        for num in arr2:
            for _ in range(arr2_dic[num]):
                ans.append(num)
        not_in.sort()
        print(ans)
        
        return  ans + not_in


         
        