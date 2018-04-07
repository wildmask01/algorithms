class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        lis = list(str(x))

        if lis[0] == '-':
            lis = lis[1:]
            token = '-'
        else:
            token = ''

        new_lis = []
        lis_len = len(lis)
        for index in range(0, lis_len, 1):
            r_index = lis_len - index - 1
            if lis[r_index] != 0:
                new_lis.append(lis[r_index])

        r_str = ''.join(new_lis[1:])
        if lis_len == 10:
            if token == '-':
                if new_lis[0] > str(2) or (new_lis[0] == str(2) and r_str > '147483648'):
                    return 0
            else:
                if new_lis[0] > str(2) or (new_lis[0] == str(2) and r_str > '147483647'):
                    return 0

        r_str = token + ''.join(new_lis)
        return int(r_str)


if __name__ == '__main__':
    sol = Solution()
    res = sol.reverse(1563847412)
    print res
