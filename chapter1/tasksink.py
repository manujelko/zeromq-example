import sys
import time

import zmq

context = zmq.Context()

# socket to receive messages on
receiver = context.socket(zmq.PULL)
receiver.bind("tcp://*:5558")

# wait for start of batch
s = receiver.recv()

# start our clock now
tstart = time.time()

# process 100 confirmations
for task_nbr in range(100):
    s = receiver.recv()
    if task_nbr % 10 == 0:
        sys.stdout.write(":")
    else:
        sys.stdout.write(".")
    sys.stdout.flush()


tend = time.time()
print(f"Total elapsed time: {(tend - tstart)*1000} msec")
