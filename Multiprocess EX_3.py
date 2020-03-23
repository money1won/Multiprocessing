# EX_3
# Same as EX_2 but it calculates a cube of the input "x" Arg

from multiprocessing import Process
def cube(my_numbers):
   for x in my_numbers:
      print('%s cube  is  %s' % (x, x**3))
if __name__ == '__main__':
   my_numbers = [3, 4, 5, 6, 7, 8]
   p = Process(target=cube, args=(my_numbers,))
   p.start()
   p.join
   print ("Done")