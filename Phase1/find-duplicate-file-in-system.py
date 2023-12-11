class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        dic = {}
        root = ""
        f = ""
        for d in paths:
            directory = d.split()
            root = directory[0]
            for i in range(1,len(directory)):
                f = directory[i].split(".")
                # print(f)
                if f[1] not in dic:
                    dic[f[1]] = []
                dic[f[1]].append(root+"/"+f[0]+".txt")
            
        answer = [path for path in dic.values() if len(path)>1]
        return answer

        