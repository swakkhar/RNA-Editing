
instance=""
f = open('fc', 'r')
while True :

    lebel =  f.readline().rstrip()


    if lebel=="" :
        break

    tmp = lebel.split(" ")

    print(tmp)

    if tmp[13]!='0':
        instance = instance + "," + tmp[-1]
    

    #
print( instance )

w= open('features.txt' , 'w')
w.write(instance)
w.close()