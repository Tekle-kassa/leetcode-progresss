# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res1=0
        temp1=l1
        i=0
        p=10**i
        while temp1:
            p=10**i
            cur=temp1.val*p
            res1+=cur
            temp1=temp1.next
            i+=1
        res2=0
        temp2=l2
        j=0
        while temp2:
            p=10**j
            cur=temp2.val*p
            res2+=cur
            temp2=temp2.next
            j+=1
        res=res1+res2
        s=str(res)
        temp1=s[::-1]
        i=0
        res=ListNode()
        temp=res
        while i<len(temp1):
            val=int(temp1[i])
            node=ListNode(val)
            temp.next=node
            temp=temp.next
            i+=1
        return res.next