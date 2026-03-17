from typing import Optional,List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge_two(p, q):
            head = ListNode()
            curr = head
            while p is not None and q is not None:
                if p.val <= q.val:
                    curr.next = p
                    p = p.next
                else:
                    curr.next = q
                    q = q.next
                curr = curr.next
            if p is not None:
                curr.next = p
            if q is not None:
                curr.next = q
            head = head.next
            return head

        def merge_rec(A,p,r):
            if r-p==2:
                return merge_two(A[p],A[p+1])
            if r-p==1:
                return A[p]
            q=(p+r)//2
            merge_rec(A,p,q)
            merge_rec(A,q,r)
            return merge_two(A[p],A[q])
        return merge_rec(lists,0,len(lists))
