class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        for i in range(len(heights)):
            change = i
            for j in range(i,len(heights)):
                
                if heights[change] < heights[j]:
                    change = j

            heights[i],heights[change] = heights[change],heights[i]
            names[i],names[change] = names[change],names[i]     
        print(names)
        print(heights)
        return names
        
        
            


         