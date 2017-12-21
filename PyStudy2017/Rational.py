#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# author:tlm

class Rational(object):
    # 求最大公约数
    @classmethod
    def maxComDivision(cls, a, b):
        while b:
            a, b = b, a % b

        return a

    def __init__(self, p, q):
        gcd = Rational.maxComDivision(p, q)
        self.p = p / gcd
        self.q = q / gcd

    def __add__(self, r):
        return Rational(self.p * r.q + self.q * r.p, self.q * r.q)

    def __sub__(self, r):
        return Rational(self.p * r.q - self.q * r.p, self.q * r.q)

    def __mul__(self, r):
        return Rational(self.p * r.p, self.q * r.q)

    def __div__(self, r):
        return Rational(self.p * r.q, self.q * r.p)

    def __str__(self):
        return '%s/%s' % (self.p, self.q)

    __repr__ = __str__

    def __int__(self):
        return self.p // self.q

    def __float__(self):
        return self.p * 1.0 / self.q


def demo():
    r1 = Rational(1, 2)
    r2 = Rational(1, 4)
    print r1 + r2
    print r1 - r2
    print r1 * r2
    print r1 / r2

    print float(Rational(7, 2))
    print int(Rational(7, 2))

if __name__ == '__main__':
    demo()
