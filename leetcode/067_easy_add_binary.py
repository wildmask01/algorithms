class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a_num = int(int(a, 2))
        b_num = int(int(b, 2))
        ab_sum = a_num + b_num
        return str(bin(ab_sum))[2:]


# int(a), int(a, 2)
# bin(a) => 0b10, oct(a) => 0o2, hex(a) => 0x2
