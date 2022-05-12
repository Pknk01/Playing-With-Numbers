from random import shuffle
import serial as SRL
import numpy.random as Rand

file_path =  "/Users/victor/Desktop/Coding Projects/Sorting Algorythims /Values.txt" #Value Filepath

#---- Serial Communication ----

Valuewritecap = 10 #Caps how many writes we have to avoid memory problems
minval = 0
maxval = 10

with open(file_path, 'w') as file:

    val = range(minval, maxval, 1)
    shuffle(val)

    file.writelines(["{}\n".format(i) for i in val])

print("Write limit reached")