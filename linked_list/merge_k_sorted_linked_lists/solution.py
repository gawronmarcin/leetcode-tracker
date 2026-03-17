from typing import Optional,List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

"""
Task:
You are given an array of k linked lists lists, where each list is sorted in ascending order.

Return the sorted linked list that is the result of merging all of the individual linked lists.

Approach: Divide and Conquer
---------------------------
This solution uses a recursive merge strategy similar to Merge Sort. 
By splitting the list of K linked lists into halves, we reduce the 
number of merge operations, achieving a time complexity of O(N log k), 
where N is the total number of nodes and k is the number of lists.
"""
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
            left=merge_rec(A,p,q)
            right=merge_rec(A,q,r)
            return merge_two(left,right)
        if not lists:
            return None
        return merge_rec(lists,0,len(lists))
