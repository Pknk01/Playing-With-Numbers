# Bogosort: Randomizes array, checks if sorted, repeats if not
# O = (n-1)n!

import time
from random import shuffle
import matplotlib.pylab as pylab
import matplotlib.pyplot as PLT
import Utilities as Utilities

# ---- Variables ----

#Takes File Path to .txt file from Utilities script
RawFilePath = Utilities.RawValPath          
SortedfilePath = Utilities.SortedValPath    

valuearray = 0  #empty declaration
Arraywrites = 0
elapsedtime = 0

#Y/N prompt, saves bool as true if answer = Y (not case sensitive)
visualize = bool(str(input("\nDo you wish to visualize the sort? \nY/N \n")).upper() == "Y")

# --- Graph ---
pylab.gcf().canvas.manager.set_window_title("Bogosort Visualizer") #Sets title of graph window

# --- Sorting loop ---

with open(RawFilePath, 'r') as File:

    StartTime = time.process_time() #Stores starting time value to get total time in the end of sort
    valuearray = [int(i) for i in File.readlines()]

    while (not Utilities.isSorted(valuearray)):

        shuffle(valuearray)     #Bogosort Implementation lol
        Arraywrites += 1        #adds to shuffle count
        elapsedtime = time.process_time() - StartTime
        
        Utilities.PlotOrLogSort(visualize, valuearray, elapsedtime, Arraywrites)

# --- Outputs ---

#Stores values in file
with open(SortedfilePath, 'w') as File:
    File.writelines([f"{i}\n" for i in valuearray])

if(visualize):
    PLT.pause(0.01)
    PLT.show()

print(f"\n Elapsed Time = {round(elapsedtime, 5)}s \n Writes = {Arraywrites} \n Comparisons = {Utilities.comparisons} \n ")