##
## Imprima la cantidad de registros por cada mes.
##
## 01,3
## 02,4
## 03,2
## 04,4
## 05,3
## 06,3
## 07,5
## 08,6
## 09,3
## 10,2
## 11,2
## 12,3
##
data=open('data.csv', 'r').readlines()
data=[line.replace('\t', ';') for line in data]
#data=[line[:1] for line in data]
data = [line.split(';')[2] for line in data]
h=0
fila=[str(column[5])+str(column[6]) for column in data]
fil=sorted(set(fila))
for h in fil:
  print("{},{}".format(h, fila.count(h)))
