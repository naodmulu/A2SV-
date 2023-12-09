class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        answer = []
        position = []

        for i in range(len(boxes)):
            if boxes[i] == "1":
                position.append(i)

        for i in range(len(boxes)):
            step = 0
            for p in position:
                step += abs(p-i)

            answer.append(step)

        return answer

