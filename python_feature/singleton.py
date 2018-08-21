class Singleton(object):
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance

class MyClass(Singleton):
    a = 1

import gc

if __name__ == '__main__':
    one = MyClass()
    two = MyClass()
    print(one == two)
    print(one is two)
    print(id(one))
    print(id(two))
    del one
    gc.collect()
    print(id(two))
    # print(id(one))
