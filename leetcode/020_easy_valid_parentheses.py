class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l = {'(', '{', '['}
        r = {')', '}', ']'}

        map_dict = {'(': ')', '{': '}', '[': ']'}

        paren = []

        for char in s:
            if char in l:
                paren.append(char)
            elif char in r:
                if paren and char == map_dict.get(paren[-1]):
                    paren.pop()
                else:
                    return False
            else:
                return False

        return len(paren) == 0