# -*- coding: utf-8 -*-
from greenlet import  greenlet
from flask import signals,sessions
from greenlet import getcurrent as get_ident
sessions['xxx']='a'

# def  test1():
#     print(1)
#     gr2.switch()
#     print(3)
#
# def test2():
#     print(2)
#     gr1.switch()
#     print(4)
# gr1=greenlet(test1)
# gr2=greenlet(test2)
# gr1.switch()
# name1=gr1.getcurrent()
# print(name1)
# print(dir(greenlet.getcurrent()))
class Test(object):
    __slots__ = ("__storage__", "__ident_func__")

    def __init__(self):
        object.__setattr__(self, "__storage__", {})
        object.__setattr__(self, "__ident_func__", get_ident)
        # object.__setattr__(self,"__storage__local",local)
    def __getattr__(self, name):
        try:
            return self.__storage__[self.__ident_func__()][name]
        except KeyError:
            raise AttributeError(name)



    def __setattr__(self, name, value):
        ident = self.__ident_func__()
        storage = self.__storage__
        try:
            storage[ident][name] = value
        except KeyError:
            storage[ident] = {name: value}
    def __call__(self,name):
        print('this is call')


class Czc(object):
    def __init__(self):
        self._local=Test()

class Foo(object):
    def bar(self,message):
        print(message)

class Fii(Foo):
    def bar(self,message):
        super().bar(message)


class Fee(Fii):
    def bar(self,message):
        super().bar(message)






f=Fee()
f.bar("aaa")
# t=Test()
# t.stack=rv=[]
# ctx={'head':'v1'}
# rv.append(ctx)
# print(t.stack[-1])
# ctx['host']='www.bilibili.com'
#
# print(t.stack[-1])
#
# l=[1,2,3,4]
# print(l.pop())



