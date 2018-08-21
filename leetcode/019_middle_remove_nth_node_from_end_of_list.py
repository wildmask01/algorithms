class Solution1:
    def removeNthFromEnd(self, head, n):
        def remove(head):
            if not head:
                return 0, head
            i, head.next = remove(head.next)
            return i+1, (head, head.next)[i+1 == n]
        return remove(head)[1]


class Solution2:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        offset = 1
        fake_head = target = ListNode(0)
        cur = target.next = head

        while cur.next:
            cur = cur.next
            if offset >= n:
                target = target.next
            offset += 1

        target.next = target.next.next

        return fake_head.next