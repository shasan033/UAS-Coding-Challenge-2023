import socket

HOST = "127.0.0.1"
PORT = 9090

# Get GPS data file
with open("missionwaypoints.txt") as f:
    gps_coordinates = f.read()
    print(f"Parsed GPS coordinates: \n{gps_coordinates}")

# Create websocket for server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print("Listening to clients...")
    client, addr = s.accept()
    with client:
        print(f"Connected to {addr}")
        while True:
            client.sendall(gps_coordinates.encode("utf-8"))