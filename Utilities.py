import matplotlib.pyplot as PLT
import pathlib

# --- Global Components ---

RawValPath = str(pathlib.Path(__file__).parent.resolve()) + "/Values/RawValues.txt"
SortedValPath = str(pathlib.Path(__file__).parent.resolve()) + "/Values/SortedValues.txt"

comparisons = 0

# Re-useable function meant to be run in main while sorting loop
# Opening graph slows down efficiency, logging is faster, but not visual
def PlotOrLog(plot, array, elapsedtime, writes):

    if(plot):
        PLT.suptitle(f"Comparisons: {comparisons} | Writes = {writes} \n Elapsed Time = {round(elapsedtime, 5)}s")
        PLT.cla() #Clears current drawing in graph
    
        PLT.plot(array, 'ro')    #Draws red dots over values
        PLT.plot(array)          #Draws line joining values
        PLT.pause(0.001)          #refreshes graph with timed interval (seconds)
    else:
        print(f"Comparisons: {comparisons} | Writes = {writes} | Elapsed Time = {round(elapsedtime, 5)}s")

# Re-usable function to check if the current array is sorted
# Meant to be run in main while sorting loop
def isSorted(array):
    current_index = 0
    previous_index = 0
    global comparisons #To be able to keep track of all comparisons made, declared as global

    while(current_index < len(array)):
        
        if(array[current_index] < array[previous_index]): 
            comparisons += current_index
            return False
        
        #moves on to next index of array
        previous_index = current_index
        current_index += 1

    comparisons += current_index #adds number of comparisons based of how many checks were made
    return True #SortReturn(comparisons = comparisons, isSorted = True)