# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        obj=[]
        i=0
        temp=head
        
        while temp and temp.next:
            if temp in obj:
                return True
            
            obj.append(temp)
            i+=1
            temp=temp.next
        return False