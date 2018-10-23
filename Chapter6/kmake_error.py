#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 01:48:33 2018

@author: zel0rd
"""

import sys
import zlib
import hashlib
import os

def main() :
    if len(sys.argv) != 2 :
        print('Usage : kmake.py [file]')
        return
    
    fname = sys.argv[1]
    tname = fname
    
    fp = open(tname, 'rb')
    buf = fp.read()
    fp.close()
    
    buf2 = zlib.compress(buf)
    
    buf3 = ''
    #print(buf2)
    for c in buf2:
        #print(c)
        buf3 += chr(ord(chr(c)) ^ 0xFF) #형변환 확인하기 (error 수정)
        
    buf4 = 'KAVM' + buf3
    
    print("Print buf4 : " + buf4)
    #f = buf4.decode('utf-8')
    for i in range(3):
        md5 = hashlib.md5()
        md5.update(f)
        f = md5.hexdigest()
        
    buf4 += f
    
    kmd_name = fname.split('.')[0] + '.kmd'
    fp = open(kmd_name, 'wb')
    fp.write(buf4)
    fp.close()
    
    print('%s -> %s' % (fname, kmd_name))
    
if __name__ == '__main__' : 
    main()
    