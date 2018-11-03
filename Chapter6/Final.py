#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 10:38:58 2018

@author: zel0rd
"""

import sys
import os
import hashlib
import zlib
import StringIO

VirusDB = []
vdb = []
vsize = []

def DecodeKMD(fname):
    try:
        fp = open(fname, 'rb')
        buf = fp.read()
        fp.close()
        
        buf2 = buf[:-32]
        fmd5 = buf[-32:]
        
        f = buf2
        for i in range(3):
            md5 = hashlib.md5()
            md5.update(f)
            f = md5.hexdigest()
            
            
        if f != fmd5:
            raise SystemError
            
        buf3 = ''
        for c in buf2[4:]:
            buf3 += chr(ord(c) ^ 0xFF)
            
        buf4 = zlib.decompress(buf3)
        print("decoded")
        return buf4
    except:
        pass

    return None

def LoadVirusDB():
    buf = DecodeKMD('virus.kmd')
    fp = StringIO.StringIO(buf)
    
    while True:
        line = fp.readline()
        if not line: break
    
        line = line.strip()
        VirusDB.append(line)
    
    fp.close()
    
def MakeVirusDB():
        
    