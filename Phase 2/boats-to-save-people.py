class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        indexone = 0
        indextwo = len(people)-1
        boats = 0
        people.sort()
        while indextwo >= indexone:
            place_left = limit - people[indextwo]
            indextwo -= 1
            if indextwo >= indexone and place_left >= people[indexone]:
                indexone += 1
            boats += 1 
        return boats


