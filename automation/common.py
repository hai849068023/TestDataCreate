# -*- coding: utf-8 -*-
__author__ = 'liuxu'
__date__ = '2019/3/12 13:35'
from random import choice


# 生成随机数
def ranNumber(digits):
    number = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    rannumber = ''
    for i in range(digits):
        a = choice(number)
        rannumber = rannumber + a
    return rannumber


# 生成随机字符串
def ranStr(digits):
    str = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
           'q', 'i', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z']
    ranstr = ''
    for i in range(digits):
        a = choice(str)
        ranstr = ranstr + a
    return ranstr
