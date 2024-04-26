import sys
import time

import zmq

context = zmq.Context()

# socket to receive messages on
receiver = context.socket(zmq.PULL)
receiver.connect("tcp://localhost:5557")

# socket to send messages to
sender = context.socket(zmq.PUSH)
sender.connect("tcp://localhost:5558")

# process tasks forever
while True:
    s = receiver.recv()

    # simple progress indicator for the viewer
    sys.stdout.write(".")
    sys.stdout.flush()

    # do the work
    time.sleep(int(s) * 0.01)

    # send results to sink
    sender.send(b"")
