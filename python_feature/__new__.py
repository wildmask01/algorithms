class Foo(object):
    def __init__(self, *args, **kwargs):
        ...
    def __new__(cls, *args, **kwargs):
        return object.__new__(cls)



A = Foo('a')
B = Foo('b')