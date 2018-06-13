# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        head1 = l1
        head2 = l2
        head = cur = ListNode(0)
        while head1 or head2:
            if head1 is None:
                cur.next = head2
                break
            elif head2 is None:
                cur.next = head1
                break
            else:
                if head1.val <= head2.val:
                    newNode = ListNode(head1.val)
                    head1 = head1.next
                else:
                    newNode = ListNode(head2.val)
                    head2 = head2.next
                cur.next = newNode
                cur = cur.next
        return head.next