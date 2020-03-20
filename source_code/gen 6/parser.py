# -*- coding: utf-8 -*-
"""
Created on Sat Aug 25 10:54:28 2018

@author: HiddenDimension
"""
import re

 



def createData(algo):
    with open(algo+'.txt') as f:
        
        lines = f.readlines()
    

    p= re.compile("\d+")

    a = p.findall(lines[-2])
    b = p.findall(lines[-1])

    tp = int(a[0])/(int(a[0])+int(a[1]) )
    fp = int(b[1])/(int(b[0])+int(b[1]) )

    acc = (int(a[0])+int(b[1]) )/(int(a[0])+int(a[1])+int(b[0])+int(b[1]) )
    
    return algo+","+str(tp*100)+","+str(fp*100)+","+str(acc*100)+"\n"



algo = ['nb' ,'ada' , 'ht' ,'rf' ,'smo' ,'bagg']

headers= ["Algorithm name", "Sn(%)","Sp(%)","Accuracy(%)"]

data=""

for x in headers:
    data=data+x+","

data=data[:-1]+"\n"

for x in algo:
    data= data+createData(x)
    
    
f = open("compiled.csv", "w")
f.write(data)
f.close();
