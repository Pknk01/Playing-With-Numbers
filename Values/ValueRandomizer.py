from random import shuffle
import Utilities as utilities

file_path = utilities.RawValPath  #Value Filepath

minval = 1
maxval = 10

with open(file_path, 'w') as file:

    val = list(range(minval, maxval + 1))
    shuffle(val)

    file.writelines(["{}\n".format(i) for i in val])

print("Values Randomized")