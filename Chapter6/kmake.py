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

def main():
    
    if len(sys.argv) != 2:
        print('Usage:antivirus.py [file]')
        exit(0)
    
    fname = sys.argv[1]
    tname = fname
    #print("tname : %s" % tname)

    
    fp = open(tname, 'rb')
    buf = fp.read()
    #print("buf : %s " % buf)
    fp.close()
    
    buf2 = zlib.compress(buf)
    #print("buf2 : %s" % buf2)

    
    buf3 = ''
    for c in buf2:
        buf3 += chr(c ^ 0xFF)
        
    #print("buf3 : %s " % buf3)

    buf4 = 'KAVM' + buf3
    
    f = buf4.encode()
    #print("buf4 : %s" % buf4)
    for i in range(3):
        md5 = hashlib.md5()
        md5.update(f)
        f = md5.hexdigest().encode()
        
    f += f
    
    
    kmd_name = fname.split('.')[0] + '.kmd'
    fp = open(kmd_name, 'wb')
    fp.write(f)
    fp.close()
    
    print("%s ===>>> %s" % (fname,kmd_name))
    
if __name__ == '__main__':
    main()
    
    