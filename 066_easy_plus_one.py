class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        add_bit = 1
        digits.reverse()
        digits.append(0)

        for index in range(0, len(digits)):
            add_res = digits[index] + add_bit
            digits[index] = add_res % 10
            if add_res == 10:
                add_bit = 1
            else:
                break
        if digits[-1] == 0:
            digits.pop()

        digits.reverse()
        return digits