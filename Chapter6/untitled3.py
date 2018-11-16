#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 01:32:54 2018

@author: zel0rd

participant = ["ddd","ccc","aaa","fff","ggg","hhh"]
completion = ["ggg","hhh","fff","aaa","ccc"]

a = ["marina", "josipa", "nikola", "vinko", "filipa"]
b = ["josipa", "filipa", "marina", "nikola"]

c = ["leo", "kiki", "eden"]
d = ["eden", "kiki"]

e = ["mislav", "stanko", "mislav", "ana"]
f = ["stanko", "ana", "mislav"]

#def solution(participant, completion):
#    for i in completion:
#        participant.remove(i)
#    return participant[0]
    
    
"""
def solution(participant, completion):
    participant.sort()
    completion.sort()
    print(participant)
    print(completion)
    for i in range(len(participant)-1):
        print(participant[i] + ' ' + completion[i])
        if participant[i] != completion[i]:
            return participant[i]
        else:
            return participant[-1]