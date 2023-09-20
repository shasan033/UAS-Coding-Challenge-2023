# GPS Speed Challenge (B-GPS-0)

This is the implementation of the System Coding Challenge for UAS. The server that sends the GSP coordinates is located in `gps-server.py`. The GPS processing module is located in `gps_processor.py`.

The distance is calculated using the haversine formula, used for determining distances between two points on a globe. The server and client interacts through web sockets locally on port 9090. 