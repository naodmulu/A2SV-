# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        # find length
        length = 0
        trav = head
        while trav:
            length += 1
            trav = trav.next
        print(length,length//k,length%k)

        # find steps and extra
        step = length//k
        extra = length%k

        # start spliting
        trav = head 
        ans = []
        for _ in range(k):
            ans.append(trav)

            # determine size
            size = step
            if extra:
                size += 1
                extra -= 1
                
            i = 0
            while trav and i < size-1:
                trav = trav.next
                i += 1
            
            # disconnect the last node
            if trav:
                temp = trav.next
                trav.next = None
                trav = temp
                
        return ans
