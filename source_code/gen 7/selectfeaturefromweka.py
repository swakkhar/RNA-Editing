import re
instance=""
f = open('lr.txt', 'r')


p=re.compile("-?[0-9]+.[0-9]+")

aset = list()

while True :

    lebel =  f.readline().rstrip()


    if lebel=="" :
        break

    tmp = lebel.split(" ")

    #print(p.findall(lebel))

    #if float(tmp[13])>0:
       # instance = instance + "," + tmp[0]
    
    if float(p.findall(lebel)[0])>=0:
        instance = instance + "," + tmp[0]
        aset.append(tmp[0])
        #print(tmp[0]+"\n")
        

    #
#print( instance )



f = open('slf.txt', 'r')


p=re.compile("-?[0-9]+.[0-9]+")



while True :

    lebel =  f.readline().rstrip()


    if lebel=="" :
        break

    tmp = lebel.split(" ")

    #print(p.findall(lebel))

    #if float(tmp[13])>0:
       # instance = instance + "," + tmp[0]
    
    if float(p.findall(lebel)[0])>=0:
        instance = instance + "," + tmp[0]
        
        v = tmp[0][1:-1]
        
        aset.append(v)
        #print(v)
        

    #
#print( instance )






f = open('J48.txt', 'r')


p=re.compile("[ACGU0-9{}\[\]]+")



while True :

    lebel =  f.readline().rstrip()


    if lebel=="" :
        break

    tmp = lebel.split(" ")

    #print(p.findall(lebel)[0])
    aset.append(p.findall(lebel)[0])

    #if float(tmp[13])>0:
       # instance = instance + "," + tmp[0]
    
    #if float(p.findall(lebel)[0])>0:
     #   instance = instance + "," + tmp[0]
        

    #
#print( sorted(aset) )



import pandas as pd

f=pd.read_csv("trainL gen 6.csv")






newList = list((aset))
newList.append("Adenosine")



dif = ["A","AC","GA","AUC","AUG","ACUC","AUUG","CCGG","CGCA","CGGG","GUCG","UCAA","UCAG","UGAA","A[ACGU]{1}A","A[ACGU]{1}AG","C[ACGU]{1}AU","G[ACGU]{1}AU","G[ACGU]{1}CA","G[ACGU]{1}GC","AA[ACGU]{1}A","AA[ACGU]{1}CA","AC[ACGU]{1}CG","AG[ACGU]{1}UA","AU[ACGU]{1}A","CG[ACGU]{1}AU","GA[ACGU]{1}UG","GC[ACGU]{1}AU","GG[ACGU]{1}U","GU[ACGU]{1}C","GU[ACGU]{1}CA","UA[ACGU]{1}AA","UC[ACGU]{1}AU","UC[ACGU]{1}GG","A[ACGU]{2}A","A[ACGU]{2}AG","A[ACGU]{2}UA","G[ACGU]{2}GU","G[ACGU]{2}UG","AA[ACGU]{2}AG","AC[ACGU]{2}A","AU[ACGU]{2}GC","AU[ACGU]{2}GG","CG[ACGU]{2}A","GA[ACGU]{2}A","GA[ACGU]{2}UG","GC[ACGU]{2}AG","GC[ACGU]{2}GU","GC[ACGU]{2}UU","GU[ACGU]{2}AU","UA[ACGU]{2}A","UA[ACGU]{2}AA","UC[ACGU]{2}GG","UU[ACGU]{2}AG","A[ACGU]{3}AC","A[ACGU]{3}AG","A[ACGU]{3}CG","G[ACGU]{3}AU","U[ACGU]{3}CU","AA[ACGU]{3}GA","AC[ACGU]{3}UG","AG[ACGU]{3}AG","AU[ACGU]{3}A","CG[ACGU]{3}CG","CG[ACGU]{3}UA","UA[ACGU]{3}CG","UC[ACGU]{3}C","UC[ACGU]{3}AU","UC[ACGU]{3}CA","UU[ACGU]{3}GU","U[ACGU]{4}CA","AA[ACGU]{4}AG","AA[ACGU]{4}UG","CC[ACGU]{4}G","CG[ACGU]{4}C","CG[ACGU]{4}G","GA[ACGU]{4}UA","GC[ACGU]{4}AA","GU[ACGU]{4}UC","UA[ACGU]{4}A","UC[ACGU]{4}GU","UU[ACGU]{4}AU","C[ACGU]{5}GC","G[ACGU]{5}UG","U[ACGU]{5}AA","U[ACGU]{5}GA","AA[ACGU]{5}GA","AC[ACGU]{5}AA","AC[ACGU]{5}AG","AC[ACGU]{5}CA","AC[ACGU]{5}GG","AG[ACGU]{5}GA","AU[ACGU]{5}AA","AU[ACGU]{5}UC","CG[ACGU]{5}U","CG[ACGU]{5}UC","GG[ACGU]{5}A","GG[ACGU]{5}AC","UA[ACGU]{5}CC","UC[ACGU]{5}G","UC[ACGU]{5}AU","UC[ACGU]{5}GU","A[ACGU]{6}A","C[ACGU]{6}UU","AA[ACGU]{6}AU","AC[ACGU]{6}A","AC[ACGU]{6}AA","CG[ACGU]{6}UG","CU[ACGU]{6}GG","GG[ACGU]{6}A","GG[ACGU]{6}GU","UC[ACGU]{6}AC","A[ACGU]{7}A","A[ACGU]{7}AC","A[ACGU]{7}UG","G[ACGU]{7}AU","AA[ACGU]{7}AC","AU[ACGU]{7}GC","AU[ACGU]{7}GG","CA[ACGU]{7}U","CA[ACGU]{7}UG","CG[ACGU]{7}CG","CG[ACGU]{7}GU","GG[ACGU]{7}CC","UA[ACGU]{7}AU","UG[ACGU]{7}C","A[ACGU]{8}G","G[ACGU]{8}U","U[ACGU]{8}C","U[ACGU]{8}GG","AA[ACGU]{8}CA","AC[ACGU]{8}A","AC[ACGU]{8}AA","CC[ACGU]{8}CU","CG[ACGU]{8}CC","GC[ACGU]{8}UA","GG[ACGU]{8}G","GG[ACGU]{8}CU","GG[ACGU]{8}GU","GG[ACGU]{8}UG","UA[ACGU]{8}U","UA[ACGU]{8}UU","UC[ACGU]{8}UC","A[ACGU]{9}A","C[ACGU]{9}CU","C[ACGU]{9}GG","G[ACGU]{9}U","G[ACGU]{9}GU","G[ACGU]{9}UC","G[ACGU]{9}UG","U[ACGU]{9}UC","U[ACGU]{9}UU","AA[ACGU]{9}AC","AA[ACGU]{9}GU","AG[ACGU]{9}GA","CC[ACGU]{9}AU","CU[ACGU]{9}CG","GG[ACGU]{9}UG","UC[ACGU]{9}GU","UG[ACGU]{9}GG","UU[ACGU]{9}A","UU[ACGU]{9}UC","A[ACGU]{10}A","A[ACGU]{10}AG","A[ACGU]{10}CA","A[ACGU]{10}UC","C[ACGU]{10}AU","C[ACGU]{10}CG","C[ACGU]{10}GA","U[ACGU]{10}G","U[ACGU]{10}CU","U[ACGU]{10}GC","AG[ACGU]{10}AG","AU[ACGU]{10}CU","AU[ACGU]{10}GU","CA[ACGU]{10}UC","CC[ACGU]{10}AG","CG[ACGU]{10}UC","CU[ACGU]{10}AA","CU[ACGU]{10}GC","GA[ACGU]{10}UC","GU[ACGU]{10}CU","GU[ACGU]{10}GU","UA[ACGU]{10}CG","UC[ACGU]{10}CA","UG[ACGU]{10}AU",'UG[ACGU]{10}CG',"Adenosine"]

for d in dif:
    if d not in newList:
        print(d)
