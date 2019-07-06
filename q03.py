##
## Imprima la suma de la columna 2 por cada letra de la 
## primera columna, ordneados alfabeticamente.
##
## A,37
## B,36
## C,27
## D,23
## E,67
data=open('data.csv', 'r').readlines()
j=0
letra = sorted(set([line[0] for line in data]))
for j in letra:
    total = sum([int(line[1]) for line in data if line[0] == j])
    letra=sorted(letra)
    print ("{},{}".format (str(j), str(total)))
