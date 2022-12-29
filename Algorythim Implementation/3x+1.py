# 3x+1: if even divide by two, if not multiplies by 3 and adds one 

import matplotlib.pyplot as PLT
import matplotlib.pylab as pylab

# --- Values ---

Iterations = 10
StepIterations = bool(input("\nDo you wish to step through each iteration?\nY/N \n").upper() == "Y")

PeakValueArray = []
LengthValueArray = []

# --- Plot Window ---
pylab.gcf().canvas.manager.set_window_title("3x+1 Visualizer") #Sets title of graph window

def PlotWindow(maxvalue, valuecount, array, iteration):
    PLT.suptitle(f"Iteration Peak: {maxvalue} | Iteration Length: {valuecount} | Iteration Number {iteration}")
    PLT.cla()
    PLT.plot(array, 'ro')
    PLT.plot(array)
    PLT.pause(0.01)

# --- Algorythm Function for cleanliness ---

def ThreeXPlusOne(input):
    
    currval = input
    array = []

    while(currval != 1):
        
        if(currval % 2 == 0):   #Divides by two if value is even
            currval /= 2
        else:                   # 3x + 1
            currval = (currval * 3) + 1

        array.append(currval) #stores to value array
        
        maxval = max(array)
        count = len(array)
        
        PlotWindow(maxval, count, array, input) #Plots window with current values

    # --- keeping values in global scope ---
    global PeakValueArray, LengthValueArray
    PeakValueArray.append(maxval)
    LengthValueArray.append(count)

# --- Main while loop ---

while (Iterations >= 1):
    
    ThreeXPlusOne(Iterations)       #Runs algorythm unitll reaching 1 for Input number

    if(StepIterations):             #waits for a buttonpress before iterating on the next value
        PLT.waitforbuttonpress()

    Iterations -= 1                 #decreases index of iterations and loops

#--- output ---

pylab.gcf().canvas.manager.set_window_title("Peak Length Values & Length Values vs Iteration Index") #Sets title of graph window
PLT.suptitle(f"All-Time Peak Value : {max(PeakValueArray)} | All-time longest iteration {max(LengthValueArray)}\n Red = Length Values | Blue = Peak Values")
PLT.xlabel("Array Data")
PLT.ylabel("Iteration Index")

PLT.scatter(PeakValueArray, range(1, len(PeakValueArray) + 1), color='blue')
PLT.scatter(LengthValueArray, range(1, len(LengthValueArray) + 1), color='red')

PLT.pause(0.01) #updates window one last time
PLT.show()      #keeps the window from closing after finishing the looping