class Solution1:

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        from functools import reduce
        letters = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        return list(reduce(lambda acc, digit: [x + y for x in acc for y in letters[int(digit)]], digits, ['']))


class Solution2:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        letters = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        sols = ['']
        for digit in digits:
            sols = [prefix + letter for letter in letters[int(digit)] for prefix in sols]
        return sols


class Solution3:
    letters = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
            return []
        if len(digits) == 1:
            return list(self.letters[int(digits[0])])
        prev = self.letterCombinations(digits[:-1])
        return [prefix + letter for letter in self.letters[int(digits[-1])] for prefix in prev]



