##
## Imprima la suma de la segunda columna.
##
data=open('data.csv', 'r').readlines()
data
cont=0
i=0
col=[column[2] for column in data]
for i in col:
  cont=cont+int(i)
print(cont)
