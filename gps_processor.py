import haversine as hs
from haversine import Unit
import pandas as pd
import socket

HOST = "127.0.0.1"
PORT = 9090

# Create client socket
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((HOST, PORT))
gps_coordinates = clientSocket.recv(4096).decode()

# Take server data and parse it
df = pd.DataFrame([map(float, x.split("\t")) for x in gps_coordinates.split("\n")])
print(f"Parsed information from server: \n{df}")

speed = []
for i in range(len(df) - 2):
    loc1 = df.iloc[i]
    loc2 = df.iloc[i + 1]
    distance = hs.haversine(loc1, loc2, unit=Unit.METERS)
    speed.append(distance)

average_speed = sum(speed) / len(speed)
print(f"Average speed (m/s): {average_speed}")