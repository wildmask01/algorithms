# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    @staticmethod
    def from_list(lst):
        head = cur = ListNode(0)
        for val in lst:
            cur.next = ListNode(val)
            cur = cur.next
        return head.next

    def to_list(self):
        lst = []
        node = self
        while node:
            lst.append(node.val)
            node = node.next
        return lst


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
            cur_val = l1_val + l2_val + add_bit
            cur.next = ListNode(cur_val % 10)
            add_bit = 1 if cur_val >= 10 else 0
            l1 = l1.next if l1 else l1
            l2 = l2.next if l2 else l2
            cur = cur.next
        return head.next


test_cases = [{'l1': ListNode.from_list([2, 4, 3]), 'l2': ListNode.from_list([5, 6, 4])}]

if __name__ == '__main__':
    sol = Solution()
    for test_case in test_cases:
        list_node = sol.addTwoNumbers(test_case['l1'], test_case['l2'])
        print(list_node.to_list())

