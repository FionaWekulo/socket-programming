#Building in the socket communication assignment,
#create two processes P and Q that have logical clocks which increment at different rates.
# Both should send each other a message at random. When a process receives a message, 
#it should update it's logical clock appropriately.



from os import getpid #to get the process id of each process
from datetime import datetime #to get the current time
from multiprocessing import Process, Pipe #to run multiple Python processes with one script

#prints the local Lamport timestamp and the actual time on the machine executing the processes
def local_time(count):
    return ' (LAMPORT_TIME={}, LOCAL_TIME={})'.format(count, datetime.now())

#new timestamp when a process receives a message. 
#The function takes the maximum of the received timestamp and its local count, and increments it with one
def get_receive_time(receive_time, count):
    return max(receive_time, count) + 1

# function for every event that may occur
#event takes the local count and the process id (pid), increments the count by one, 
#prints a line so we know the event took place and returns the incremented count.
def event(pid, count):
    count = count + 1
    print('\n\n****************************************EVENT*************************************\nAn event took place at {} '.\
          format(pid) + local_time(count))
    return count

#sending_message event first increments the count by one,
#Then sends an actual message and its incremented timestamp, 
#and prints a short statement including the new local Lamport time and the actual time on the machine.
def sending_message(pipe, pid, count):
    count += 1
    pipe.send(('Hello world!', count))
    print('A message was sent from ' + str(pid) + local_time(count))
    return count


#receiving_message receives both the actual message and the timestamp by invoking the recv function on the pipe. 
#Then it calculates the new timestamp with our previously created get_receive_time function, 
#and prints a line including the updated count and the actual time on the machine.
def receiving_message(pipe,pid,count):
    message, timestamp = pipe.recv()
    count = get_receive_time(timestamp, count)
    print('The message was received at ' + str(pid) + local_time(count))
    return count

#creating the definitions of the 2 processes
def P(pipe112):
    pid = getpid() #getting its unique process id
    count = 0 #setting its own count to 0
    count = event(pid, count) #count gets updated by invoking the different event functions
    count = sending_message(pipe112, pid, count)
    count = event(pid, count)
    count = receiving_message(pipe112, pid, count)
    count = event(pid, count)

def Q(pipe211):
    pid = getpid()
    count = 0
    count = receiving_message(pipe211, pid, count)
    count = sending_message(pipe211, pid, count)

if __name__ == '__main__':
    PandQ, QandP = Pipe()

    processP = Process(target=P,
                       args=(PandQ,))
    processQ = Process(target=Q,
                       args=(QandP,))

#To start the processes
    processP.start()
    processQ.start()

#Join assures us that all processes will be completed before quitting.
    processP.join()
    processQ.join()

