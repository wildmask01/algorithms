import heapq
# nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
# print(heapq.nlargest(3, nums)) # Prints [42, 37, 23]
# print(heapq.nsmallest(3, nums)) # Prints [-4, 1, 2]


# heap=[2, 4, 3, 5, 7, 8, 9, 6]
# heapq.heapreplace(heap, 1)
# print(heap)
#
#
# heap=[2, 4, 3, 5, 7, 8, 9, 6]
# heapq.heappushpop(heap, 1)
# print(heap)


# a = (1, 0 ,2)
# b = (1, 2, 0)
# c = (5, 1, 2)


# sorted()

# class A(object):
#     class_var = 1
#     def __init__(self):
#         self.name = 'xy'
#         self.age = 2
#
#     @property
#     def num(self):
#         return self.age + 10
#
#     def fun(self):pass
#     def static_f():pass
#     def class_f(cls):pass
#
# if __name__ == '__main__':#主程序
#     a = A()
#     print(a.__dict__)  #{'age': 2, 'name': 'xy'}   实例中的__dict__属性
#     print(A.__dict__)



# prices = {
#     'ACME': 45.23,
#     'AAPL': 612.78,
#     'IBM': 205.55,
#     'HPQ': 37.20,
#     'FB': 10.75
# }
#ddddd   ddddddddddd
# price_and_names = zip(prices.values(), prices.keys())
# result = max(price_and_names)
# print(result)


# def dedup(item_list):
#     seen = set()
#     for item in item_list:
#         if item not in seen:
#             yield item
#             seen.add(item)
#
#
# items = [1, 3, 3, 3, 4, 5]
#
# print(list(dedup(items)))

# from collections import Counter
#
# a = ['hello', 'hello', 'wold']
# word_count = Counter(a)
# print(word_count.most_common(1))

#
# from collections import namedtuple
#
# haha = namedtuple('stock', ['name', 'addr'])
#
#
# record = ('xiao', 'ming')
#
# s = haha(*record)
#
# print(s)


#
# a = [1, 2, 3]
# b = [3, 4, 5]
#
# res = [x*y for x in a for y in b]
# print(res)
# print(sum(x*y for x in a for y in b))


# text = 'foo = 23 + 42 * 10'
# import re
# from collections import namedtuple
#
# NAME = r'(?P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)'
# NUM = r'(?P<NUM>\d+)'
# PLUS = r'(?P<PLUS>\+)'
# TIMES = r'(?P<TIMES>\*)'
# EQ = r'(?P<EQ>=)'
# WS = r'(?P<WS>\s+)'
# master_pat = re.compile('|'.join([NAME, NUM, PLUS, TIMES, EQ, WS]))
#
# def generate_tokens(pat, text):
#     Token = namedtuple('Token', ['type', 'value'])
#     scanner = pat.scanner(text)
#     for m in iter(scanner.match, None):
#         yield Token(m.lastgroup, m.group())
#
#
# for tok in generate_tokens(master_pat, 'foo = 42'):
#     print(tok)

# scanner = master_pat.scanner('foo = 42')


#
# lst = [1, 2, 3]
#
# iterator = iter(lst)
#
# while True:
#     num = next(iterator, None)
#     if num is None:
#         break
#     print(num, end='\n')
#
# def count_down(n):
#     while n>0:
#         yield n
#         n -= 1
#
#
# c = count_down(3)
# for n in c:
#     print(n)


# data = [(1, 2), (3, 4), ]
# for key, (x, y) in enumerate(data):
# 	print(x, y)
#

#
# xlst = [1, 4, 8]
# ylst = [3, 6, 9]
#
# tu = dict(zip(xlst, ylst))
# print(tu)


#
# from collections import Iterable
#
# def flatten(items):
#     for x in items:
#         if isinstance(x, Iterable):
#             yield from flatten(x)
#         else:
#             yield x
#
# items = [1, 2, [3, 4, [5, 6], 7], 8]
#
# print(list(flatten(items)))

# def apply_async(func, args, *, callback):
#     result = func(*args)
#
#     callback(result)



## 协程

# def consumer():
#     r = ''
#     while True:
#         n = yield r
#         if not n:
#             return
#         print('[CONSUMER] Consuming %s...' % n)
#         r = '200 OK'
#
# def produce(c):
#     c.send(None)
#     n = 0
#     while n < 5:
#         n = n + 1
#         print('[PRODUCER] Producing %s...' % n)
#         r = c.send(n)
#         print('[PRODUCER] Consumer return: %s' % r)
#     c.close()
#
# c = consumer()
# produce(c)


# stack = []
# stack.append('[')
# print(stack)
#
# if isinstance('hell', str):
#     print('hell')
#


# str = ""
# for char in str:
#     print(char)
#
# def generateParenthesis(n):
#     """
#     :type n: int
#     :rtype: List[str]
#     """
#     # '(':
#
#     target_list = []
#     target_list.append({'': [0, 0, 0]})
#
#     return list(target_list[0].keys())
#     #
#     # for index in range(1, 2 * n + 1):
#     #     for sol, prop in target_list[index - 1].items():
#     #         if prop[0] < n:
#     #             new_sol = sol + '('
#     #             target_list[index].update({new_sol: [prop[0] + 1, prop[1], prop[2] + 1]})
#     #         if prop[1] < n and prop[2] > 0:
#     #             new_sol = sol + ')'
#     #             target_list[index].update({new_sol: [prop[0], prop[1] + 1, prop[2] - 1]})
#     #
#     # return target_list[2 * n].keys()
#
#
# # print(generateParenthesis(0))
#
# # dict1 = {'22': 22, '33':33}
#
#
# new_list = [None] * 10
# print(new_list[0])
# # target_list = []
# # target_list.append({'': [0, 0, 0]})

#
# s = 'hello world'
#
# list_s = s.split(' ')
# for word in list_s.reverse():
#     if word:
#         return len(word)


# def convert(s, numRows):
#     """
#     :type s: str
#     :type numRows: int
#     :rtype: str
#     """
#     level = 1
#     direction = 'down'
#
#     res_list = []
#     cur_dict = {}
#
#     for char in s:
#         cur_dict.update({level: char})
#
#         if direction == 'down':
#             level += 1
#             if level > numRows:
#                 direction = 'up'
#                 level -= 2
#                 res_list.append(cur_dict)
#                 cur_dict = {}
#
#         if direction == 'up':
#             level -= 1
#             res_list.append(cur_dict)
#             cur_dict = {}
#             if level == 1:
#                 direction = 'down'
#
#     final_string = ''
#     for level in range(1, numRows + 1):
#         for char_dict in res_list:
#             if char_dict.get(level):
#                 final_string += char_dict.get(level)
#
#     return str(res_list)
#
#
# convert()


# def longestPalindrome(s):
#     """
#     :type s: str
#     :rtype: str
#     """
#     if len(s) < 1:
#         return s
#
#     s = ''.join([char + '#' for char in list(s)])[:-1]
#
#     max_str = ""
#     max_offset = 0
#     s_len = len(s)
#
#     for cur_index in range(0, s_len):
#         offset = 0
#         while cur_index - offset >= 0 and cur_index + offset < s_len:
#             if s[cur_index - offset] == s[cur_index + offset]:
#                 if offset > max_offset:
#                     max_str = s[cur_index - offset:cur_index + offset + 1]
#                     max_offset = offset
#                 offset += 1
#             else:
#                 offset = s_len  # break inner loop
#
#     return max_str.replace('#', '')
#
#
# print(longestPalindrome("abb"))

# int('1-')

# def threeSumClosest(nums, target):
#     """
#     :type nums: List[int]
#     :type target: int
#     :rtype: int
#     """
#     nums.sort()
#     closest_sum = sum(nums[0:3])
#     dif = abs(target - closest_sum)
#
#     nums_len = len(nums)
#     for i in range(0, nums_len - 2):
#         if i > 0 and nums[i] == nums[i - 1]:
#             continue
#         j = i + 1
#         k = nums_len - 1
#         while j < k:
#             tmp_sum = nums[i] + nums[j] + nums[k]
#             tmp_dif = abs(tmp_sum - target)
#             if tmp_dif < dif:
#                 closest_sum = tmp_sum
#             if tmp_sum == target:
#                 break
#             elif tmp_sum < target:
#                 j += 1
#             else:
#                 k -= 1
#     return closest_sum
#
# threeSumClosest([0,2,1,-3], 1)


# def twoSum(nums, target):
#     """
#     :type nums: List[int]
#     :type target: int
#     :rtype: List[int]
#     """
#
#     l = 0  # left
#     r = len(nums) - 1  # right
#     nums.sort()
#
#     solutions = []
#
#     while l < r:
#         if nums[l] + nums[r] == target:
#             solutions.append([l, r])
#             while l < r and nums[l + 1] == nums[l]:
#                 l += 1
#             while l < r and nums[r - 1] == nums[r]:
#                 r -= 1
#             l += 1
#             r -= 1
#         elif nums[l] + nums[r] < target:
#             l += 1
#         else:
#             r -= 1
#
#     return solutions[0]
#
#
# twoSum([3,2,4], 6)

# l = ['(', '{', '[']
# r = [')', '}', ']']
#
# map_dict = zip(l, r)
#
# print(dict(map_dict))

# import dis
#
# def func(a,b):
#     a,b=b,a
#     print(a,b)
#
# a=10
# b=20
# func(a,b)
# dis.dis(func)


# def divide(dividend, divisor):
#     """
#     :type dividend: int
#     :type divisor: int
#     :rtype: int
#     """
#     sign = ''
#     if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0):
#         sign = '-'
#
#     dividend = abs(dividend)
#     divisor = abs(divisor)
#
#     lst = []
#     while divisor <= dividend:
#         lst.append(divisor)
#         divisor += divisor
#
#     quotient = 0
#     pow_value = len(lst) - 1
#
#     for index, divisor in enumerate(lst[::-1]):
#         if dividend >= divisor:
#             quotient += pow(2, pow_value - index)
#             dividend -= divisor
#
#     return int(sign + str(quotient - 1))
#
#
# divide(-10, -5)

#
# def nextPermutation(nums):
#     """
#     :type nums: List[int]
#     :rtype: void Do not return anything, modify nums in-place instead.
#     """
#     num_len = len(nums)
#     if not nums or len(nums) == 1:
#         return nums
#
#     for index in range(len(nums) - 1, 0, -1):
#         if nums[index] > nums[index - 1]:
#             break
#
#     if index - 1 == 0 and nums[0] > nums[1]:
#         return nums.sort()
#
#     for k in range(len(nums) - 1, 0, -1):
#         if nums[k] > nums[index - 1]:
#             break
#
#     nums[k], nums[index - 1] = nums[index - 1], nums[k]
#     end = (num_len - 1 - index) // 2 + 1
#
#     for k in range(0, end):
#         nums[index + k], nums[num_len - k] = nums[num_len - k], nums[index + k]
#
#     return nums
#
# nextPermutation([1,4,3, 2, 3, 3])



#
# def searchRange(nums, target):
#     """
#     :type nums: List[int]
#     :type target: int
#     :rtype: List[int]
#     """
#     if not nums:
#         return [-1, -1]
#
#     def find_edge(edge_type):
#         lo, hi = 0, len(nums) - 1
#         while lo <= hi:
#             mid = (lo + hi) // 2
#             if nums[mid] == target:
#                 if edge_type == 'low':
#                     if mid > 0 and nums[mid - 1] == target:
#                         hi = mid - 1
#                     else:
#                         return mid
#                 else:
#                     if mid < len(nums) - 1 and nums[mid + 1] == target:
#                         low = mid + 1
#                     else:
#                         return mid
#             elif nums[mid] > target:
#                 hi = mid - 1
#             else:
#                 lo = mid + 1
#         return -1
#
#     low_edge = find_edge('low')
#     high_edge = find_edge('high')
#
#     return [low_edge, high_edge]
#
#
# searchRange([2, 2], 2)


#
# from pyhive import hive
# conn = hive.Connection(host="39.106.251.31", port=10000, username="root", database='hivetest')
# cursor = conn.cursor()
# cursor.execute("select * from employee")
# for result in cursor.fetchall():
#     print(result)



# from functools import wraps
#
#
# def memo(fn):
#     cache = {}
#     miss = object()
#
#     @wraps(fn)
#     def wrapper(*args):
#         result = cache.get(args, miss)
#         if result is miss:
#             result = fn(*args)
#             cache[args] = result
#         return result
#
#     return wrapper
#
#
# @memo
# def fib(n):
#     if n < 2:
#         return n
#     return fib(n - 1) + fib(n - 2)
#
# print(fib(3))




#
# order_list = [
#     {'order_id': 1, 'price': 100, 'date': '2018-01-01'},
#     {'order_id': 2, 'price': 200, 'date': '2018-01-02'},
#     {'order_id': 3, 'price': 300, 'date': '2018-01-05'},
#     {'order_id': 4, 'price': 400, 'date': '2018-01-01'},
# ]
#
# import pandas as pd
#
# df = pd.DataFrame(order_list)
# df['month'] = df['date'].apply(lambda x : str(x)[5:7])
# print(df['price'].values.tolist())
# print([1, 2])

# import pandas as pd
# import numpy as np
# df = pd.DataFrame(np.arange(16).reshape((4,4)), index=['one', 'two', 'three', 'four'], columns=['a', 'b', 'c', 'd'])
#
# # df = df.apply(lambda x: x.max() + x.min(), axis=1)  # 1 是对行聚合
# # df = df.apply(lambda x: x.max() + x.min(), axis=0)  # 0 是对列聚合， 默认为0
#
# df['e'] = df.apply(lambda x: x['a'] + x['b'], axis=1)
# print(df)
# print(df[df['price'] > 200])




# class Date:
#     _formats = {
#         'ymd': '{d.year}-{d.month}-{d.day}',
#         'mdy': '{d.month}/{d.day}/{d.year}',
#         'dmy': '{d.day}/{d.month}/{d.year}'
#     }
#     def __init__(self, year, month, day):
#         self.year = year
#         self.month = month
#         self.day = day
#
#     def __format__(self, code):
#         if code == '':
#             code = 'ymd'
#         fmt = self._formats[code]
#         return fmt.format(d=self)
#
#
# d = Date(2012, 12, 21)
# print(format(d))
# print(format(d, 'ymd'))
# print(format(d, 'mdy'))