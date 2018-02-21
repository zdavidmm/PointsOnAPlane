import socket
import gen_points as gp
import time

host = socket.gethostname()
port = 10256                   # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
while True:
    s.sendall(gp.genOut())
    data = s.recv(1024)
    print('Received', repr(data))
    time.sleep(3)
