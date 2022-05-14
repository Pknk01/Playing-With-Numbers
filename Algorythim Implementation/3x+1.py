# 3x+1: if even divide by two, if not multiplies by 3 and adds one 

import matplotlib.pyplot as PLT
import matplotlib.pylab as pylab

# --- Plot Window ---
pylab.gcf().canvas.manager.set_window_title("3x+1 Visualizer") #Sets title of graph window

def PlotWindow(maxvalue, valuecount, array):
    PLT.suptitle(f"Peak Value: {maxvalue} | Value Count: {valuecount}")
    PLT.cla()
    PLT.plot(array, 'ro')
    PLT.plot(array)
    PLT.pause(0.01)

# --- Values ---

Iterations = 10

# --- Main while loop ---

while (Iterations > 0):
    
    CurrentValue = Iterations   # starts loop
    Maxvalues = []              # max value array
    Valuecounts = []            # Array of how many digits are per iteration
    Valuearray = []             # Array of 3x+1 values, resets per iteration

    while (CurrentValue > 1):
        
        if(CurrentValue % 2 == 0):                      # if even divide by two
            CurrentValue /= 2
        else:                                           # if odd, multiply by 3 add 1
            CurrentValue = (CurrentValue * 3) + 1

        Valuearray.append(CurrentValue)                 # Appends values of this tteration
    
    Maxvalue.append()
    
        



while (CurrentValue > 1):

    if(CurrentValue % 2 == 0): 
        CurrentValue /= 2 
    else:
        CurrentValue = (CurrentValue * 3) + 1
    
    ValueArray.append(CurrentValue)
    maxvalue = max(ValueArray)
    valuecount = len(ValueArray)



#--- output ---

PLT.show() #keeps the window from closing after finishing the looping