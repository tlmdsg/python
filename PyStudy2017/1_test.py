#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# author:tlm

from __future__ import division
import math


def demo():
    # 1.数据结构
    print(45678 + 0x12fd2)
    print('Learn Python in imooc')
    print(100 < 99)
    print(0xff == 255 and 1 == 2)
    print(1.23e12 / 10)
    print(None)

    print(u'''
      静夜思

    床前明月光，
    疑是地上霜。
    举头望明月，
    低头思故乡。''')

    # 2.列表、元组
    if "Hello" or True:
        print(True)
    print("hello" or True)

    l = ['Adam', 'Lisa', 'Bart']
    l.append('Paul')
    l.insert(2, 'Paul')
    l.pop(2)
    l.remove('Paul')
    l[2] = 'paul'
    print(l)

    t = tuple(range(10))
    print(t)

    # 3.切片
    L = range(1, 101)
    print(L[-10:])
    print(L[-46::5])

    # 4.列表生成式
    print([x * 100 + y * 10 + z \
           for x in range(1, 10) \
           for y in range(0, 10) \
           for z in range(0, 10) \
           if x == z])


def average(*args):
    length = len(args)
    sums = 0
    print(sum([1, 2]))
    if length == 0:
        return
    else:
        for i in args:
            sums += i
        return sums / length


if __name__ == '__main__':
    demo()
    # print average
    # print sum([1,2])
    # print type(range(100))
    # print average()
    # print average(1, 2)
    # print average(1, 2, 2, 3, 4)
