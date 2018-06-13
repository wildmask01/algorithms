class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left = set('[{(')
        right = set(']})')
        couple = {
            ']': '[',
            '}': '{',
            ')': '(',
        }
        stack = []
        for char in s:
            if char in left:
                stack.append(char)
            elif char in right:
                if len(stack) == 0:
                    return False
                pop_ele = stack.pop()
                if pop_ele != couple[char]:
                    return False
            else:
                return False
        return len(stack) == 0