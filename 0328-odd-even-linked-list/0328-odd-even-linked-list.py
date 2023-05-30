# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        oddTail=head
        evenList=head.next
        evenHead=evenList
      
        while evenList and evenList.next:
            oddTail.next=evenList.next
            oddTail=oddTail.next
            evenList.next=oddTail.next
            evenList=evenList.next
        oddTail.next=evenHead
        return head
            