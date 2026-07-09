# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        dummy =ListNode(0)
        current=dummy
        curr1 = list1
        curr2 = list2

        while curr1 is not None and curr2 is not None:
            if curr1.val  < curr2.val:
                current.next = curr1
                curr1 =curr1.next
            else:
                current.next = curr2
                curr2 = curr2.next
            current =current.next

        if curr1 is not None:
            current.next = curr1
        else:
            current.next = curr2
            

        return dummy.next

        