# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        less_head = ListNode(0)
        greater_head = ListNode(0)
        less_tail = less_head
        greater_tail = greater_head
        current = head
        while current:
            if current.val < x:
                less_tail.next = current
                less_tail = less_tail.next
            else:
                greater_tail.next = current
                greater_tail = greater_tail.next
            current = current.next
        less_tail.next = greater_head.next
        greater_tail.next = None

        return less_head.next
                
        