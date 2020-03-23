# EX_5
# This example uses pipes
# Pipes are used to communicate between 2 processes
# Think of it as 2 ends of a pipe and the connection between them that a pipe provides

from multiprocessing import Process, Pipe
def myfunction(conn):
   conn.send(['hi!! I am Python'])  # Sends the message to the other end of the pipe
   conn.close()
if __name__ == '__main__':
   parent_conn, child_conn = Pipe()  # These are your two ends of the pipe
   p = Process(target=myfunction, args=(child_conn,))
   p.start()
   print (parent_conn.recv() ) # The end of the pipe not used in the process receives info sent
   p.join()


# https://www.tutorialspoint.com/multiprocessing-in-python