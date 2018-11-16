#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 01:26:54 2018

@author: zel0rd
"""

def solution(a, b):
    answer = 0
    if(a > b):
        a , b = b , a
    for i in range(abs(a-b) + 1):
        answer = answer + a + i
        print(answer)
    return answer