from random import shuffle
import time
import matplotlib.pylab as LAB
import matplotlib.pyplot as PYPLT

#Summary: Bogosort Randomizes array, checks if sorted, repeats if not. O = (n-1)n!

ETStart = time.process_time() #stores start time to calculate total elapsed time

# --- Vars ---

Rawfilepath = "/Users/victor/Desktop/Coding Projects/Sorting Algorythims /Values.txt"
Sortedfilepath = "/Users/victor/Desktop/Coding Projects/Sorting Algorythims /SortedValues.txt"

values = 0          #Value Array
arraywrites = 0     #number of writes to array
comparisons = 0
visualize = True

# --- Visualizer ---

LAB.gcf().canvas.manager.set_window_title("Bogosort Visualizer")  #Sets title of window

# --- Sorting Loop ---

def isSorted(array):

    curr_index = 0
    prev_index = 0
    global comparisons

    while (curr_index < len(array)):

        if (array[curr_index] < array[prev_index]):
            comparisons += curr_index
            return False

        prev_index = curr_index
        curr_index += 1

    comparisons += curr_index #adds all comparisons
    return True

with open(Rawfilepath, 'r') as file:

    values = [int(i) for i in file.readlines()] #Stores value array from file

    while (not isSorted(values)):

        shuffle(values)     #Bogosort Implementation (lol)
        arraywrites += 1
        ETEnd = time.process_time()
        ExecutionTime = ETEnd-ETStart

        if(visualize):
            PYPLT.suptitle("Comparisons = {} | Shuffles = {} \nProcess Time = {}s".format(comparisons, arraywrites, round(ExecutionTime, 4))) #Info Text
            PYPLT.cla()
            PYPLT.plot(values, range(0, len(values)))     #refreshes graph with second interval
            PYPLT.plot(values, range(0, len(values)), 'ro')
            PYPLT.pause(0.001)


# --- Outputs ---

#Stores sorted values in file
with open(Sortedfilepath, 'w') as file:
    file.writelines(["{}\n".format(val) for val in values])


if(visualize):
    PYPLT.waitforbuttonpress()

print("\n Excecution Time = {} \Shuffles: {}\n Comparisons: {}".format(ExecutionTime, arraywrites, comparisons))
