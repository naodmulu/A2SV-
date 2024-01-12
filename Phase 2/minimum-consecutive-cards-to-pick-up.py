class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        length = float("inf")
        occur = {}
        for r in range(len(cards)):
            if cards[r] in occur:
                length = min(length,r - occur[cards[r]]+1)
                occur[cards[r]] = r
            else:
                occur[cards[r]] = r
        
        if length == float("inf"):
            return -1
        else:
            return length

        