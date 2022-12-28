import random
import concurrent.futures
import time
import threading
import itertools
import sys

# Constants and the timing function
start = time.perf_counter()
global finalResults
finalResults = []
global totalThreadRuns
totalThreadRuns = []
totalRuns = 0

# Initialisation values
numberOfThreads = 100
global runsToComplete
runsToComplete = 100000000
#These sum to 10,000,000,000 (10 billion)

def Bag():
    validRuns = 0
    global totalRuns
    for totalRuns in range (runsToComplete):
        bag = [3,3,3,3,3,3,3,3,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,1,0]
        output = 0
        for x in range (3):
            index = random.randint(0,len(bag)-1)
            arrayNum = bag[index]
            output = output + arrayNum
            bag.pop(index)
        if  output == 4:
            validRuns = validRuns + 1
        totalRuns = totalRuns + 1
    totalThreadRuns.append(totalRuns)
    average = (validRuns / totalRuns)
    finalResults.append(average)

done = False

# Outputs the current number of runs every 30s so I can have a progress log on how each of the threads are doing
def Check():
    while done == False:
        print("{:,}".format(len(totalThreadRuns) * runsToComplete), " runs completed of ", "{:,}".format(numberOfThreads * runsToComplete), " runs")
        time.sleep(30)

# Runs the check as an isolated thread to not block the current process
t = threading.Thread(target=Check)
t.start()

# Thread pool executor runs daemon threads by default
with concurrent.futures.ThreadPoolExecutor() as executor:
    if __name__ == '__main__':
        for x in range (numberOfThreads):
            threadIdNumber = str(x + 1)
            threadName = "Thread"
            threadString = threadName + threadIdNumber
            threadString = executor.submit(Bag)
            
# Threads do not shutdown because I forgot to code that in
done = True

# Outputs inportant information to the console
print("")
print(finalResults)
print("The net average:  ", (sum(finalResults) / numberOfThreads))
print("Time taken:  ", (time.perf_counter() - start))

# Finds out how many iterations of the program have been logged before
with open('output.txt', 'r') as f:
    NumberOfLines = len(f.readlines())
    
# Logs everything to the text file
with open('output.txt', 'a') as f:
    print("------------------------------", file=f)
    NumberOfOutPuts = "Version number:  " + str((NumberOfLines / 10) + 1)
    print(NumberOfOutPuts, file = f)
    print("------------------------------", file=f)
    OutputRuns = "Runs:  " + str(runsToComplete)
    OutputNetAverage = "Average:  " + str((sum(finalResults) / numberOfThreads))
    OutputThreads = "Threads:  " + str(numberOfThreads)
    OutputIterations = "Iterations:  " + str(runsToComplete)
    OutputArrayAccesses = "Array accesses:  " + str((runsToComplete * numberOfThreads * 5))
    OutputTimeTaken = "Time taken:  " + str((time.perf_counter() - start))
    print(OutputRuns, file=f)
    print(OutputNetAverage, file=f)
    print(OutputThreads, file=f)
    print(OutputIterations, file=f)
    print(OutputArrayAccesses, file=f)
    print(OutputTimeTaken, file=f)
    print("------------------------------", file=f)
