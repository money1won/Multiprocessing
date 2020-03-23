# EX_2
# Same as EX_1, however it passes an argument through the process

from multiprocessing import Process
def display(my_name):
   print ('Hello' + " " + my_name)
if __name__ == '__main__':
   p = Process(target=display, args=('Python',))   # Args is where "my_name" would pull from
   p.start()
   p.join()