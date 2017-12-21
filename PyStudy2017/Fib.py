#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# author:tlm

class Fib(object):
    # 构造定长的斐波那契数列
    @classmethod
    def constructFib(cls, length):
        result = [0, 1]
        for i in range(1, length - 1):
            result.append(result[i - 1] + result[i])
        return result

    def __init__(self, length=None):
        if length:
            self.length = length
            self.fib = Fib.constructFib(length)

    def __str__(self):
        return self.fib.__str__()

    __repr__ = __str__

    def __len__(self):
        return len(self.fib)

    def __call__(self, length, *args, **kwargs):
        return Fib.constructFib(length)


def demo():
    f = Fib(10)
    print f
    print len(f)

    f= Fib()
    print f(10)

if __name__ == '__main__':
    demo()
