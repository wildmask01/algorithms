class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        level = 1
        direction = 'down'

        res_list = []
        cur_dict = {}

        for char in s:
            cur_dict.update({level: char})

            if direction == 'down':
                level += 1
                if level > numRows:
                    direction = 'up'
                    level -= 2
                    res_list.append(cur_dict)
                    cur_dict = {}

            if direction == 'up':
                level -= 1
                res_list.append(cur_dict)
                cur_dict = {}
                if level == 1:
                    direction = 'down'

        final_string = ''
        for level in range(1, numRows + 1):
            for char_dict in res_list:
                if char_dict.get(level):
                    final_string += char_dict.get(level)

        return str(res_list)