# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        i=0
        dummy=ListNode()
        dummy.next=head
        r=1
        temp=dummy.next
        while temp.next:
            r+=1
            temp=temp.next
        idx=r-n 
        temp2=dummy.next
        print(temp2)
        if idx==0:
            dummy.next=temp2.next
            return dummy.next
        while temp2 and i<idx-1:
            temp2=temp2.next
            i+=1
         
        if temp2 and temp2.next:
            temp2.next=temp2.next.next
        return dummy.next
            
            