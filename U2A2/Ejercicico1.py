#Exercise 1: Using the multithreading module, write a simple python 
#program as follows:
#Create a pool of threads to run concurrent tasks.
#The pool size should be 10.
#The thread should receive as input a number [id]
#(unique identifier for each of the
#threads, starting from 1) and a number [number_of_writtings] 
#(number of times the thread will write the message).

def accion(thread_id, num_writtings):
    