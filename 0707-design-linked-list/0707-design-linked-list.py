class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
class MyLinkedList:

    def __init__(self):
        self.l=Node(0)
    def get(self, index: int) -> int:
        temp=self.l.next
        while temp and index>0:
            temp=temp.next
            index-=1
        if temp and index==0:
            return temp.val
        return -1

            

    def addAtHead(self, val: int) -> None:
        node=Node(val)
        temp=self.l.next
        node.next=temp 
        self.l.next=node
        

    def addAtTail(self, val: int) -> None:
        node=Node(val)
        temp=self.l
        while temp.next:
            temp=temp.next
        temp.next=node
            

    def addAtIndex(self, index: int, val: int) -> None:
        node=Node(val)
        temp=self.l.next
        if index==0:
            self.l.next=node
            node.next=temp
            return
        i=0
        while temp and i<index-1:
            temp=temp.next
            i+=1
        if temp:
            if temp.next:
                target=temp.next
                temp.next=node
                node.next=target
            else:
                temp.next=node

    def deleteAtIndex(self, index: int) -> None:
        i=0
        temp=self.l.next
        if index==0:
            self.l.next=temp.next
            return
        while temp and i<index-1:
            temp=temp.next
            i+=1
        if temp:
            if temp.next:
                target=temp.next
                temp.next=target.next
            

        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)