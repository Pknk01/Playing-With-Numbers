from random import shuffle
import Utilities as utilities

file_path = utilities.RawValPath  #Value Filepath

min_val = 1
max_val = 10

with open(file_path, 'w') as file:

    val = list(range(min_val, max_val + 1))
    shuffle(val)

    file.writelines(["{}\n".format(i) for i in val])

print("Values Randomized")