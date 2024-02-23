class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        # print(deck)
        que = deque(range(len(deck)))
        ans = [ 0 for _ in deck]
        i = 0
        while i < len(deck):
            # print(que,i)
            # print(ans)
            temp = que.popleft()
            ans[temp] = deck[i] 
            if que:
                que.append(que.popleft())
            i += 1

        return ans