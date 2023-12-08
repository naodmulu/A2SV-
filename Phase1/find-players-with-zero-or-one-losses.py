class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        players = set()
        count = {}
        answer = [[],[]]
        for match in matches:
            players.add(match[0])
            players.add(match[1])

        for player in players:
            count[player] = 0
        
        for win,loss in matches:
            if loss in count:
                count[loss] += 1

        for key,value in count.items():
            if value == 0:
                answer[0].append(key)
            elif value == 1:
                answer[1].append(key) 

        print(count)
        answer[0].sort()
        answer[1].sort()
        return answer
        
