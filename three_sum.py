class Solution(object):
    def three_sum(self, nums):
        """
        :param self:
        :param nums:
        :return:
        """

        nums.sort()
        pre = None
        fs = []
        for key, val in enumerate(nums):
            if val == pre:
                continue
            dic = {}
            for index, num in enumerate(nums):
                if index <= key:
                    continue
                if num in dic:
                    ps = [val, -(val+num), num]
                    fs.append(ps)
                else:
                    dic[- val - num] = index
            pre = val

        final_sl = []
        ps_hash_dic = {}
        for ls in fs:
            ps_hash = ','.join([str(int_val) for int_val in ls])
            if ps_hash not in ps_hash_dic:
                final_sl.append(ls)
                ps_hash_dic.update({ps_hash: ls})

        return final_sl


if __name__ == '__main__':
    plist = [0, 0, 0, 0]
    sol = Solution()
    res = sol.three_sum(plist)
    print(res)
