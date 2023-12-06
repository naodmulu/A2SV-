class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        steps = 0
        jar = capacity
        index = 0
        while index < len(plants):
            if plants[index] <= jar:
                steps += 1
                jar -= plants[index]
                index += 1
            else:
                steps += 2*index + 1
                jar = capacity - plants[index]
                index += 1

        return steps 
        