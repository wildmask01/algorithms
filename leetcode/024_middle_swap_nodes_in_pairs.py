# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution1:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if not head or not head.next:
            return head

        cur = dummy = ListNode(0)
        l, r = head, head.next

        while l and r:
            next_node = r.next
            cur.next = r
            r.next = l
            l.next = next_node

            l = next_node
            r = l.next if l else None
            cur = cur.next.next

        cur.next = l if l else None
        return dummy.next


class Solution2:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if not head or not head.next:
            return head

        new_head = head.next
        head.next = self.swapPairs(new_head.next)
        new_head.next = head
        return new_head