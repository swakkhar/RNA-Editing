import array

f = open('data.txt', 'r')
instance = ""
rna_element =" ACGU"

def head():
    head=""
    for i in range (1 ,5 ):

        for j in range(1, 52):

            element = rna_element[i];
            head= head +","+ (element+str(j))

    return (head[1:])

def analyze_rna(rna):

    features =  [0 for p in range(205)]
    data=""
    for i in range (1 ,5 ):

        ec=0
        for j in range(1, 52):

            element = rna_element[i];
            if element == rna[j]:
                #print(rna[j]+element+str(j))
                ec=ec+1;
                data=data+","+str("yes")
            else:

                data = data + "," + "no"
    print(data[1:])
    return (data[1:])


instance=head()+",lebel\n"
while True :

    lebel =  f.readline().rstrip()
    if  "Positive" in lebel:
        lebel = 'positive'
    else :
        lebel = 'negative';

    rna = f.readline().rstrip()
    print(len(rna))

    if lebel == "" or rna=="" :
        break

    instance =instance + analyze_rna( " "+rna ) +" ,"+lebel+ "\n"
    print( instance )


w= open('e.csv' , 'w')
w.write(instance)
# head()
# analyze_rna(" UAUGGUCGCAAAGGUUUUCUUUAUUACGUUGCAGACUUCAGAAAAAAGUCA")
