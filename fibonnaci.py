#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 08:57:20 2022

@author: parisbg
"""

def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    print("n = ", n)
    return fib(n-1) + fib(n-2)

fib(4)
