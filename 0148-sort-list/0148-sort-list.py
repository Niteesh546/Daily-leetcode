# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        curr = head
        value=[]
        while curr is not None:
            v = curr.val
            value.append(v)
            curr = curr.next
        value.sort()

        current=head
        for val in value:
            current.val = val
            current = current.next

        return head



        