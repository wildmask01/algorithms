# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        add_bit = 0
        head = cur = ListNode(0)
        while l1 or l2 or add_bit:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            sum_val = l1_val + l2_val + add_bit
            new_node = ListNode(sum_val % 10)
            cur.next = new_node
            cur = cur.next
            l1 = l1.next if l1 else l1
            l2 = l2.next if l2 else l2
            add_bit = sum_val // 10

        return head.next
