#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 12:52:58 2018

@author: zelord
"""
import hashlib
import os

fp = open('DummyTest.txt','rb')
fbuf = fp.read()
fp.close()

m = hashlib.md5()
m.update(fbuf)
fmd5 = m.hexdigest()
print(fmd5)
if fmd5 == '44d88612fea8a8f36de82e1278abb02f':
    print('Virus')
    #os.remove('eicar.txt')
else :
    print('No Virus')