#!/usr/bin/env python3

from tornado.tcpserver import TCPServer
from tornado.iostream import StreamClosedError
from tornado.ioloop import IOLoop
from tornado import gen

class EchoServer(TCPServer):
    async def handle_stream(self, stream, address):
        while True:
            try:
                data = await stream.read_until(b"\n")
                await stream.write(data)
            except StreamClosedError:
                break

if __name__ == "__main__":
    server = EchoServer()
    server.listen(8000)
    IOLoop.current().start()

