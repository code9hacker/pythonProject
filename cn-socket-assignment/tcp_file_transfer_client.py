import socket
import sys
from pathlib import Path

HOST, PORT = "localhost", 9999

#data = Path("".join(sys.argv[1:])).read_text()
data = Path('tcp.txt').read_text()
print('data = '.join(data))

# create a TCP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # connect to server
    sock.connect((HOST, PORT))

    # send data
    sock.sendall(bytes(data + "\n", encoding='utf8'))

finally:
    # shut down
    sock.close()

print("Sent:     {}".format(data))
