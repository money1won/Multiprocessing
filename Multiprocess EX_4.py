# EX_4
# Follows EX_3, but now it completes this using multiple processes

from multiprocessing import Process
def cube(my_numbers):
   for x in my_numbers:
      print('%s cube  is  %s' % (x, x**3))
def evenno(my_numbers):
   for x in my_numbers:
      if x % 2 == 0:
         print('%s is an even number ' % (x))
if __name__ == '__main__':
   my_numbers = [3, 4, 5, 6, 7, 8]
   my_process1 = Process(target=cube, args=(my_numbers,))  # Defines the process for "cube"
   my_process2 = Process(target=evenno, args=(my_numbers,))  # Defines the process for evenno
   my_process1.start()  # Start the "cube" process
   my_process2.start()  # Start the "evenno" process
   my_process1.join()  # MUST use this to complete the process, or it will idle
   my_process2.join()  # Complete the process
   print ("Done")


# Both cube and evenno happen at the same time in this example