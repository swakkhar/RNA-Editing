# -*- coding: utf-8 -*-
"""
Created on Sun Aug 26 07:55:17 2018

@author: HiddenDimension
"""

import re
instance=""
f = open('J48.txt', 'r')


p=re.compile("[ACGU0-9{}\[\]]+")

aset = set()

while True :

    lebel =  f.readline().rstrip()


    if lebel=="" :
        break

    tmp = lebel.split(" ")

    print(p.findall(lebel)[0])
    aset.add(p.findall(lebel)[0])

    #if float(tmp[13])>0:
       # instance = instance + "," + tmp[0]
    
    #if float(p.findall(lebel)[0])>0:
     #   instance = instance + "," + tmp[0]
        

    #
print( sorted(aset) )

w= open('featurestree.txt' , 'w')
w.write(instance[1:])
w.close()