class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        self.prev = None
class BrowserHistory:

    def __init__(self, homepage: str):
        self.home = ListNode(homepage)
        self.curr = self.home
        
        
    def visit(self, url: str) -> None:
        newNode = ListNode(url)
        self.curr.next = newNode
        newNode.prev = self.curr
        self.curr = newNode
        # trav = self.curr
        # print("visit")
        # while trav:
        #     print(trav.val)
        #     trav = trav.prev
        # print("visit end")
        

    def back(self, steps: int) -> str:
        # trav = self.curr
        # print("back")
        # while trav:
        #     print(trav.val)
        #     trav = trav.prev
        # print("back end")
        trav = self.curr
        while steps and trav.prev:
            trav = trav.prev
            steps -= 1
        self.curr = trav
        return self.curr.val

    def forward(self, steps: int) -> str:
        # trav = self.curr
        # print("forward")
        # while trav:
        #     print(trav.val)
        #     trav = trav.prev
        # print("forward end")
        trav = self.curr
        while steps and trav.next:
            trav = trav.next
            steps -= 1
        self.curr = trav
        return self.curr.val
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)