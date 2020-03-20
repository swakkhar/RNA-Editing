f = open('difference.txt', 'r')
instance = ""
rna_element =" ACGU"

while True :


    line = f.readline().rstrip()


    if  line=="" :
        break

    instance =instance + line

items = ""


for o in instance.split(","):

    if "'" in o:
        items = items.replace("'",'"') + "," +  o
    else:
        items = items + "," + '"' + o + '"'


print( items )

w= open('f.txt' , 'w')
w.write(items[1:])
w.close()