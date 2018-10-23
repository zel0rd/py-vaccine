#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 23:33:32 2018

@author: zelord
"""

import sys
import os
import hashlib

VirusDB = [
        '68:44d88612fea8a8f36de82e1278abb02f:EICAR Test',
        '65:77bff0b143e4840ae73d4582a8914a43:Dummy Test'
        ]

vdb = []
vsize = []

def MakeVirusDB():
    for pattern in VirusDB:
        t = []
        v = pattern.split(':')
        t.append(v[0])
        t.append(v[1])
        t.append(v[2])
        vdb.append(t)
        print(t)
        
        """
        size = int(v[0])
        if vsize.count(size) == 0:
            vsize.append(size)
        """
def SearchVDB(fmd5) :
    for t in vdb:
        if t[1] == fmd5:
            return True,t[2]
    
    return False, ''


if __name__ == '__main__':
    MakeVirusDB()    #악성코드DB생성
    
    if len(sys.argv) != 2:    #커맨드라인 입력방식 체크
        print("Usage : antivirus.py [file]")
        exit(0)
        
    fname = sys.argv[1]
    
    size = os.path.getsize(fname)    #검사 대상 파일 크기
    index = 0    #검사대상과 DB에 같은 크기의 파일이 있는지 판별
    for i in range(len(vdb)):
        #print(vdb[i][0] + "  " + str(size))
        if vdb[i][0] == str(size):
            index += 1
        #print("index : %s" % index)
        
    if index > 0 :    #파일 크기가 같은경우에만 SearchVDB를 실행한다.
        fp = open(fname,'rb')
        buf = fp.read()
        fp.close()
        
        m = hashlib.md5()
        m.update(buf)
        fmd5 = m.hexdigest()
        
        ret,vname = SearchVDB(fmd5)
        if ret == True:
            print("FileName : %s , VDBName : %s" % (fname,vname))
            #os.remove(fname)
        else :
            print("%s : ok #only same size file" % (fname))
                
    else :
        print("%s : ok #not same size file" % (fname))