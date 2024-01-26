# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        odd1 = ListNode(0,None)
        even1 = ListNode(0,None)
        odd = odd1
        even = even1
        flag = 0
        if (head.val)%2:
            flag = 1
        count = 1
        while head:
            if count:
                count = 0
                odd.next = head
                odd = odd.next
            else:
                count = 1
                even.next = head
                even = even.next
            
            head= head.next
        even.next = None
        odd.next = even1.next
        return odd1.next
        


        