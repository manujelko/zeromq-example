import sys

import zmq

context = zmq.Context()
socket = context.socket(zmq.SUB)

print("Collect updates from weather server...")
socket.connect("tcp://localhost:5556")

zip_filter = sys.argv[1] if len(sys.argv) > 1 else "10001"
socket.setsockopt_string(zmq.SUBSCRIBE, zip_filter)

total_temp = 0
update_nbr = 0
for update_nbr in range(100):
    string = socket.recv_string()
    zipcode, temperature, relhumidity = string.split()
    total_temp += int(temperature)

print(
    f"Average temperature for zipcode '{zip_filter}' was "
    f"{total_temp / (update_nbr + 1)}F"
)
