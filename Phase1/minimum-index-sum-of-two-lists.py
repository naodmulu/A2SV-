class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        summ = {}
        answer = []
        for i, word in enumerate(list1):
            if word in list2:
                summ[word] = i + list2.index(word)  

        minimum = min(summ.values())  
        for key,value in summ.items():
            if value == minimum :
                answer.append(key)

        return answer
            


