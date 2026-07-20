# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        if not head and not head.next:
            return True
        fast= head
        slow=head

        while fast and fast.next:
            slow=slow.next
            fast = fast.next.next
        
        curr = slow
        prev = None
        while curr:
            next_node=curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        left=head
        right=prev

        while right:
            if left.val != right.val:
                return False
            right =right.next
            left  = left.next
        return True
        
        