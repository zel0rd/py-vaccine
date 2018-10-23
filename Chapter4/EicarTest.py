#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 12:37:53 2018

@author: zelord
"""
import os

fp = open('eicar2.txt','rb')
fbuf = fp.read()
len(fbuf)
print("\n","\n",fbuf,"\n","\n",len(fbuf))
if fbuf[0:3] == b'X5O':
    print("Virus")
    #os.remove('eicar.txt')
else :
    print("No Virus")
fp.close()