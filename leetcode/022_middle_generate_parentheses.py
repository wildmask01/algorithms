
class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # '(':

        target_list = [{'': [0, 0, 0]}]

        for index in range(1, 2 * n + 1):
            sol_dict = {}
            for sol, prop in target_list[index - 1].items():
                if prop[0] < n:
                    new_sol = sol + '('
                    sol_dict.update({new_sol: [prop[0] + 1, prop[1], prop[2] + 1]})
                if prop[1] < n and prop[2] > 0:
                    new_sol = sol + ')'
                    sol_dict.update({new_sol: [prop[0], prop[1] + 1, prop[2] - 1]})
            target_list.append(sol_dict)

        return list(target_list[2 * n].keys())


# 先初始化一个数组，再用下标更新是不行的
# lst = []; lst[0] = 1  => out of index range
# lst = []; lit.append(1)

# lst = [1, 2, 3, 4, 12]
# would be "better" than
#
# lst = [1, 2, 3, 4]
# ... # code has nothing do to with lst
# lst.append(12)
# or => this list creation could be rewritten as a list literal

# 注意 dict.keys(), dict.values(), dict.items, 都只是生成器，
# list(dict.keys()), list(dict.values())  dict(dict.items())

