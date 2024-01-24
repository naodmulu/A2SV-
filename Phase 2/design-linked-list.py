class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
        self.prev = None
class MyLinkedList:

    def __init__(self):
        self.dummy_head = Node(None)
        self.dummy_tail = Node(None)
        self.dummy_head.next = self.dummy_tail
        self.dummy_tail.prev = self.dummy_head

    def get(self, index: int) -> int:
        i = 0
        trav = self.dummy_head.next
        while i < index:
            if not trav:
                return -1
            trav = trav.next
            i += 1
        if trav and trav != self.dummy_tail:
            return trav.val
        return -1

    def addAtHead(self, val: int) -> None:
        newNode = Node(val)
        n = self.dummy_head.next
        self.dummy_head.next = newNode
        newNode.next = n
        newNode.prev = self.dummy_head
        n.prev = newNode

    def addAtTail(self, val: int) -> None:
        newNode = Node(val)
        p = self.dummy_tail.prev
        self.dummy_tail.prev = newNode
        newNode.prev = p
        newNode.next = self.dummy_tail
        p.next = newNode        

    def addAtIndex(self, index: int, val: int) -> None:
        trav = self.dummy_head.next
        while trav and index > 0:
            trav = trav.next
            index -= 1
        if index == 0 and trav:
            newNode = Node(val)
            n = trav
            p = trav.prev
            p.next = newNode
            newNode.next = n
            n.prev = newNode
            newNode.prev = p

    def deleteAtIndex(self, index: int) -> None:
        trav = self.dummy_head.next
        while trav and index > 0:
            trav = trav.next
            index -= 1
        if index == 0 and trav and trav != self.dummy_tail:
            n = trav.next
            p = trav.prev
            p.next = n
            n.prev = p
            
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)