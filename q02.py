##
## Imprima la cantidad de registros por letra para la 
## primera columna, ordenados alfabeticamente.
##
## A,8
## B,7
## C,5
## D,6
## E,14
##
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas
%matplotlib inline
data=open('data.csv', 'r').readlines()
data=[column[:-1].split("\t") for column in data]
fila=[column[0] for column in data]
letra=sorted(set(fila))
for h in letra:
  print("{},{}".format(h, fila.count(h)))
