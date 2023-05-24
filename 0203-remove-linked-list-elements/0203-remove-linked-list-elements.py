# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # start=ListNode()
        # start.next=head
        while head and head.val==val:
            head=head.next
        temp=head
        while temp and temp.next:
            if temp.next.val==val:
                temp.next=temp.next.next
                continue
            temp=temp.next
        return head