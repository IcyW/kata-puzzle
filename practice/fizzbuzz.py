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

    def say(self, x):
        self.x = x
        if self.x % self.m == 0 and self.x % self.n == 0:
            return "FizzBuzz"

        if self.x % self.m == 0:
            return "Fizz"

        if self.x % self.n == 0:
            return "Buzz"
