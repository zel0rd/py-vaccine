#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 00:27:39 2018

@author: zelord
"""

import sys
import os
import hashlib

VirusDB = []
vdb = []
vsize = []

def LoadVirusDB() :
    fp = open('virus.db', 'rb')
    
    while True:
        line = fp.readline()
        #print(line)
        if not line : break
        line = line.strip()
        VirusDB.append(line)
        
    fp.close()
    
def MakeVirusDB() :
    for pattern in VirusDB:
        t = []
        v = pattern.split(b':')
        t.append(v[1])
        #print(t)
        t.append(v[2])
        #print(t)
        vdb.append(t)
        #print(t)
        
        size = int(v[0])
        if vsize.count(size) == 0:
            vsize.append(size)
            
def SearchVDB(fmd5):
    for t in vdb:
       # print(t)
        #print("\n\n")
        #print(fmd6)
        if t[0] == fmd5:
            return True, t[1]
   
        
    return False, ''

if __name__ == '__main__':
    LoadVirusDB()
    
    MakeVirusDB()
    
    if len(sys.argv) != 2:
        print("Usage : antivirus.py [file]")
        exit(0)
        
    fname = sys.argv[1]
    #print(fname)
    print("Inspect file -> " + fname)
    size = os.path.getsize(fname)
    #print(size)
    if vsize.count(size):
        fp = open(fname,'rb')
        buf = fp.read()
        fp.close()
        
        m = hashlib.md5()
        m.update(buf)
        fmd5 = m.hexdigest().encode()
        ret, vname = SearchVDB(fmd5)
        if ret == True:
            print("%s <- It is Virus" % (fname))
            #os.remove(fname)
        else:
            print("%s : Normal File" % fname)
    else:
        print("%s : No VirusDB" % fname)