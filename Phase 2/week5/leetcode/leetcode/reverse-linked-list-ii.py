# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # print(head)
        if not head or right == left:
            return head
        ans = ListNode(0,head)
        trav = ans
        prev = None
        n = None
        index = 0
        while trav:
            if index == left:
                l = trav
                begin = None
                while trav and index <= right:
                    n = trav.next
                    trav.next = begin
                    begin = trav
                    trav = n
                    index += 1
                l.next = trav
                prev.next = begin
                break

            prev = trav
            trav = trav.next
            index += 1            
        return ans.next
        