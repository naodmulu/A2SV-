# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-5001)
        def insertion(node):
            comp = dummy
            prev = None
            while comp and comp.val < node.val:
                prev = comp
                comp = comp.next
            prev.next = node
            node.next = comp
        trav = head
        while trav:
            new = trav.next
            insertion(trav)
            trav = new
        
        return dummy.next        
        
          



        




