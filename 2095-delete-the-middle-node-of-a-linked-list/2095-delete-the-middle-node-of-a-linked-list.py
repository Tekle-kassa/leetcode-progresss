# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode()
        dummy.next=head
        slow=dummy
        fast=dummy
        temp=dummy.next 
        i=1
        while temp and temp.next:
            temp=temp.next
            i+=1
        n=i//2
        j=0
        temp=dummy.next
        if n==0:
            dummy.next=temp.next
            # return dummy.next
        else:
            while temp and j<n-1:
                temp=temp.next
                j+=1
            if temp and temp.next:
                temp.next=temp.next.next
        return dummy.next
            
        
            
        
    
    
            