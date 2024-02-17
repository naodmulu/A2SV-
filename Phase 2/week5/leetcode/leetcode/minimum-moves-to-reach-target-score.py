class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        count = 0
        temp = target
        while target != 1:
            if maxDoubles:
                if target%2 == 1:
                    count += 2
                    maxDoubles -= 1
                    target = target//2
                else:
                    count += 1
                    target = target//2
                    maxDoubles -= 1
            else:
                count += target - 1
                target = 1
            # print(target,count)

        return count