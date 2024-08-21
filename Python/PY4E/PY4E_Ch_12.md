# This is a study guide for PY4E Chapter 12

# SOCKETS IN PYTHON

import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to data.pr4e.org using PORT 80
mysock.connect( ('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.text HTTP/1.0\r\n\r\n' .encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode)