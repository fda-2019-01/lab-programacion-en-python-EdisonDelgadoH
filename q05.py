##
## Imprima el valor maximo y minimo por cada letra de la columa 1.
##
## A,9,1
## B,9,1
## C,9,0
## D,7,1
## E,9,1
##
i=0
j=0
minval=0
maxval=2
data=open('data.csv', 'r').readlines()
data=[line[0:3] for line in data]
data=[line.replace('\t', ';') for line in data]
letra = sorted(set([line[1] for line in data]))
for i in letra:
  for j in data:
    if (j[0])==(letra):
        print ("prueba")
        if maxval < j[3]:
            maxval=i[3]
        if j[2] < minval:
            minval=i[3]
  print (i, str(minval), str(maxval))
