import socketserver


class MyTCPSocketHandler(socketserver.BaseRequestHandler):

    def handle(self):
        print("{} wrote:".format(self.client_address[0]))
        self.data = self.request.recv(1024).strip()
        if self.data.decode('UTF-8').find("SECRET") != -1:
            digits = ''.join(chr(c) for c in self.data if chr(c).isdigit())
            self._result = "Digits: " + digits + " Count: " + str(len(digits))
        else:
            self._result = "Secret code not found."

        #print(self.data)
        self.request.sendall(bytes(self._result, encoding='utf8'))


if __name__ == "__main__":
    HOST, PORT = "localhost", 9999

    server = socketserver.TCPServer((HOST, PORT), MyTCPSocketHandler)

    server.serve_forever()
