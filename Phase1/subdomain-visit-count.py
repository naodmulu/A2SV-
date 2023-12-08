class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        count = {}
        temp = []
        for i in cpdomains:
            temp = list(map(str,i.split(" ")))

            count[temp[1]] = count.get(temp[1],0) + int(temp[0])
            print(count)
            for j in range(len(temp[1])):
                if temp[1][j-1] == ".":

                    count[temp[1][j:]] = count.get(temp[1][j:], 0) + int(temp[0])
        answer = []
        print(count)
        for key,value in count.items():
            temp = f"{value} {key}"
            answer.append(temp)

        return answer

