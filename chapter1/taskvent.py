import random
import time

import zmq

context = zmq.Context()

# socket to send the messages on
sender = context.socket(zmq.PUSH)
sender.bind("tcp://*:5557")

# socket with direct access to the sink: use to synchornize start of batch
sink = context.socket(zmq.PUSH)
sink.connect("tcp://localhost:5558")

print("Press Enter when the workers are ready: ")
_ = input()
print("Sending tasks to workers...")

# the first message is "0" and signals start of batch
sink.send(b"0")

random.seed()

total_msec = 0
for task_nbr in range(100):
    workload = random.randint(1, 100)
    total_msec += workload
    sender.send_string(f"{workload}")


print(f"Total expected cost: {total_msec} msec")

time.sleep(1)
