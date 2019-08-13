#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 13/8/2019 下午8:05
@Author  : Icy Huang
@Site    : 
@File    : fizzbuzz.py
@Software: PyCharm Community Edition
@Python  : 
"""


class FizzBuzz:
    def __init__(self, m, n):
        self.m = m
        self.n = n
        self.x = 1

    def is_fizz(self):
        if self.x % self.m == 0:
            return True
        m_str, x_str = str(self.m),str(self.x)
        if m_str in x_str:
            return True
        return False

    def is_buzz(self):
        if self.x % self.n == 0:
            return True
        n_str, x_str = str(self.n),str(self.x)
        if n_str in x_str:
            return True
        return False

    def say(self, x):
        self.x = x
        ans = ""
        if self.is_fizz():
            ans = "Fizz"
        if self.is_buzz():
            ans += "Buzz"

        if not ans:
            return str(x)
        else:
            return ans
