# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        have = set()
        cur = headA
        while cur:
            have.add(cur)
            cur=cur.next
        curr = headB
        while curr:
            if curr in have:
                return curr
            curr = curr.next
        
        