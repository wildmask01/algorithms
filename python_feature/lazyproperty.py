#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/14 下午6:31
# @Author  : max
# @Site    : 
# @File    : lazyproperty.py
# @Date    : 2018/8/14
# @Desc    :


class lazyproperty:
    def __init__(self, func):
        self.func = func

    def __get__(self, instance):
        if instance is None:
            return self
        else:
            value = self.func(instance)
            setattr(instance, self.func.__name__, value)
            return value


import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    @lazyproperty
    @property
    def area(self):
        print('Computing area')
        return math.pi * self.radius ** 2

    @lazyproperty
    def perimeter(self):
        print('Computing perimeter')
        return 2 * math.pi * self.radius



c = Circle(4)
print(c.area)