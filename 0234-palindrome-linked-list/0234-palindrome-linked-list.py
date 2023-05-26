# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        right=head
        res=[]
        while right.next:
            res.append(right.val)
            right=right.next
        res.append(right.val)
        l,r=0,len(res)-1
        while l<r:
            if res[l]!=res[r]:
                return False
            l+=1
            r-=1
        return True
        