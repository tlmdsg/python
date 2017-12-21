#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# author:tlm
import math


def log(f):
    def fn(*args, **kw):
        # print "\n"
        print("**********")
        print('call ' + f.__name__ + '()...')
        result = f(*args, **kw)
        print("**********")
        # print "\n"
        return result

    return fn


@log
def demo():
    # 5.函数式编程

    # 内置高阶函数 map()
    def format_name(s):
        s = s.lower()
        return s[0:1].upper() + s[1:]

    print(map(format_name, ['adam', 'LISA', 'barT']))

    # 内置高阶函数 reduce()
    def prod(x, y):
        return x * y

    print(reduce(prod, [2, 4, 5, 7, 12]))

    # 内置高阶函数 filter()
    def is_sqr(x):
        return math.sqrt(x) % 1 == 0

    print(filter(is_sqr, range(1, 101)))

    # 内置高阶函数 sorted()
    def cmp_ignore_case(s1, s2):
        s1 = s1.lower()
        s2 = s2.lower()
        if s1 > s2:
            return 1
        elif s1 == s2:
            return 0
        else:
            return -1

    def comparator(s1,s2):
        s1 = s1.lower()
        s2 = s2.lower()
        return cmp(s1,s2)

    print(sorted(['bob', 'about', 'Zoo', 'Credit'], comparator))

    # 从函数中返回函数
    def calc_prod(lst):
        def prod_callback():
            result = 1
            for i in lst:
                result *= i
            return result

        return prod_callback

    f = calc_prod([1, 2, 3, 4])
    print(f())

    # 闭包 ：这种内层函数引用了外层函数的变量（参数也算变量），然后返回内层函数的情况，称为闭包（Closure）。
    def count():
        fs = []
        for i in range(1, 4):
            def f(m=i):
                return m ** 2

            fs.append(f)
        return fs

    f1, f2, f3 = count()
    print(f1(), f2(), f3())

    # lambda匿名函数
    def is_not_empty(s):
        return s and len(s.strip()) > 0

    print(filter(lambda s: s and len(s.strip()) > 0, ['test', None, '', 'str', '  ', 'END']))

    # 装饰器 @xxx
    import time

    def performance(f):
        def fn(*args, **kw):
            print("call " + f.__name__ + "() in", time.localtime(time.time()))
            result = f(*args, **kw)
            return result

        return fn

    @performance
    def factorial(n):
        return reduce(lambda x, y: x * y, range(1, n + 1))

    print(factorial(10), factorial.__name__)

    # 装饰器 @xxx(y)
    import time, functools

    def performance(unit):
        def decorator(f):
            @functools.wraps(f)
            def fn(*args, **kw):
                print("call " + f.__name__ + "() in", str(time.time()) + str(unit))
                return f(*args, **kw)

            return fn

        return decorator

    @performance('ms')
    def factorial(n):
        return reduce(lambda x, y: x * y, range(1, n + 1))

    print(factorial(10), factorial.__name__)


if __name__ == '__main__':
    demo()
