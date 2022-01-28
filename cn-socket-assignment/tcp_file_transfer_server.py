import socketserver


class MyTCPSocketHandler(socketserver.BaseRequestHandler):

    def handle(self):
        print("{} wrote:".format(self.client_address[0]))
        self.data = self.request.recv(1024).strip()
        content = self.data.decode('UTF-8')
        text_file = open("tcp_r.txt", "w+")
        text_file.write(content)
        text_file.close()


if __name__ == "__main__":
    HOST, PORT = "localhost", 9999

    server = socketserver.TCPServer((HOST, PORT), MyTCPSocketHandler)

    server.serve_forever()
