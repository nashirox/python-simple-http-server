# https://docs.python.jp/3/library/socket.html
import socket
import request_parser as parser
import request_handler as handler

DEFAULT_HOST = '127.0.0.1'
DEFAULT_PORT = 8080

class HttpServer:
    def __init__(self, port=DEFAULT_PORT):
        self.port = port
        self.parser = parser.RequestParser()
        self.handler = handler.RequestHandler()

    def run(self):
        sever_socket = socket.socket()
        sever_socket.bind((DEFAULT_HOST, self.port))
        sever_socket.listen(1)
        print("server is listening on ", sever_socket)

        while True:
            conn, address = sever_socket.accept()
            print(address, " is accepted.")

            msg = conn.recv(4096)
            request = self.parser.parse(msg)
            print(request)
            response = self.handler.handle(request)
            conn.send(response)

            conn.close()

        sever_socket.close()

if __name__ == '__main__':
    HttpServer().run()
