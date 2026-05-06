# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy=ListNode(0)
        dummy.next=head
        prevGroup=dummy

        while True:
            if not self.hasKnodes(prevGroup.next,k):
                break
            
            groupStart=prevGroup.next
            groupEnd=groupStart

            for _ in range(k-1):
                groupEnd=groupEnd.next

            nextGroup=groupEnd.next

            groupEnd.next=None

            newHead=self.reverse(groupStart,k)

            prevGroup.next=newHead
            groupStart.next=nextGroup

            prevGroup=groupStart
        
        return dummy.next

    def reverse(self,head,k):
            prev=None
            curr=head

            while k>0:
                nxt=curr.next
                curr.next=prev
                prev=curr
                curr=nxt

                k-=1
            return prev
        
    def hasKnodes(self,head,k):
        count=0
        while head and count<k:
            head=head.next
            count +=1
            
        return count==k
        
        

            