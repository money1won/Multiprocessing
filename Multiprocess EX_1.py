# Multiprocessing
# As CPU manufacturers start adding more cores to their processors, creating parallel code is a great way to improve performance.
# Python introduced multiprocessing module to let us write parallel code.

# Module used specifically for multiprocessing
from multiprocessing import Process

# Tells you how many cpu's your computer has. Each CPU allows you to perform a process individually
# print("Number of CPU ", multiprocessing.cpu_count())

# EX_1
# Demonstrates a very simply SYNTAX of how multiprocessing works for one process

def display():  # creating a function to be made into a process you want executed
   print ('Hi !! I am Python')  # The process that will be executed
if __name__ == '__main__':  # If the code is running...
   p = Process(target=display)  # Start a "Process" (Process is imported) for func "display"
   p.start()  # Start the Process identified
   p.join()   # Complete the Process

