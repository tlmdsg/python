#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# author:tlm

class Person(object):
    __count = 0

    @classmethod
    def how_many(cls):
        return cls.__count

    def __init__(self, name=None, gender=None, birth=None, *args, **kw):
        Person.__count += 1
        self.name = name
        self.gender = gender
        # 私有属性 __birth，无法被外部访问
        self.__birth = birth
        self.args = args
        for k in kw:
            # self.__setattr__(k, kw[k])
            setattr(self, k, kw[k])
        # 此属性指向一个函数
        self.newFunction = lambda: '这是一个函数属性'

    def getBirth(self):
        return self.__birth


class Student(Person):
    def __init__(self, name=None, gender=None, birth=None, score=None, *args, **kwargs):
        super(Student, self).__init__(name, gender, birth, *args, **kwargs)
        self.__score = score
        # self.args = args
        # for k in kwargs:
        #     setattr(self, k, kwargs[k])

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, score):
        if score < 0 or score > 100:
            raise ValueError('invalid score')
        self.__score = score

    def __str__(self):
        return '(%s: %s)' % (self.name, self.__score)

    __repr__ = __str__

    # 分数从高到低排序
    def __cmp__(self, s):
        if self.__score < s.score:
            return 1
        elif self.__score > s.score:
            return -1
        else:
            return cmp(self.name, s.name)


class Teacher(Person):
    def __init__(self, name=None, gender=None, birth=None, course=None, *args, **kwargs):
        super(Teacher, self).__init__(name, gender, birth, *args, **kwargs)
        self.course = course

    def getCourse(self):
        return self.course

    def __str__(self):
        return '<Teacher: ' + self.name + ', ' + self.course + '>'

    __repr__ = __str__

    def __cmp__(self, other):
        # if self.name < other.name:
        #     return -1
        # elif self.name == other.name:
        #     return 0
        # else:
        #     return 1
        return cmp(self.name, other.name)


# 1
def test1():
    xiaoming = Person()
    xiaohong = Person()
    print xiaoming
    print xiaohong
    print xiaoming == xiaohong


# 2
def test2():
    p1 = Person()
    p1.name = 'Bart'

    p2 = Person()
    p2.name = 'Adam'

    p3 = Person()
    p3.name = 'Lisa'

    L1 = [p1, p2, p3]
    L2 = sorted(L1, lambda x, y: cmp(x.name, y.name))

    print L2[0].name
    print L2[1].name
    print L2[2].name


# 3
def test3():
    xiaoming = Student('Xiao Ming', 'Male', '1990-1-1', '88', 'arg1', 'arg2', job='Student', like='soccer')

    print xiaoming.name
    print xiaoming.getScore()
    print xiaoming.args
    print xiaoming.job
    print xiaoming.like
    print xiaoming.getScore
    print xiaoming.newFunction

    # print Person.__count
    print Person.how_many()


# 4
def test4():
    zhanglaoshi = Teacher('zhang laoshi', 'female', '1970-1-1', '物理', 'arg1', 'arg2', job='Teacher', like='basketball')
    lilaoshi = Teacher('li laoshi', 'female', '1970-1-1', '物理', 'arg1', 'arg2', job='Teacher', like='basketball')

    print zhanglaoshi.name
    print zhanglaoshi.getCourse()
    print zhanglaoshi.args
    print zhanglaoshi.job
    print zhanglaoshi.like
    print zhanglaoshi

    print isinstance(zhanglaoshi, object)
    print isinstance(zhanglaoshi, Person)
    print isinstance(zhanglaoshi, Student)
    print isinstance(zhanglaoshi, Teacher)

    print sorted([zhanglaoshi, lilaoshi])


def demo():
    pass


if __name__ == '__main__':
    test4()
