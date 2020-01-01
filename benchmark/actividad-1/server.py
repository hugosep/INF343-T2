from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import argparse
import contextlib
import datetime as dt

import grpc
import fibonacci_pb2
import fibonacci_pb2_grpc

# strings para definir servidor
_LISTEN_ADDRESS_TEMPLATE = '[::]:%d'
_SIGNATURE_HEADER_KEY = 'x-signature'
DEFAULT_PORT = 5000

# nombres
names = list()

times = list()

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

class Fibonacci(fibonacci_pb2_grpc.FibonacciServicer):

    # avisa si hay mensajes para un determinado usuario, y lo envia en caso de haberlo
    def CalcularFibo(self, requestSequence, context):
        sequence = requestSequence.sequence
        value = fib(sequence)
        return fibonacci_pb2.resposneValue(value=value)


@contextlib.contextmanager
def run_server(port):

    server = grpc.server(futures.ThreadPoolExecutor())
    fibonacci_pb2_grpc.FibonacciServicer_to_server(Fibonacci(), server)
    server.add_insecure_port(_LISTEN_ADDRESS_TEMPLATE % port)
    print('Servidor esperando en puerto :%d', DEFAULT_PORT)
    server.start()

    try:
        yield server, port

    finally:
        server.stop(0)

def main():
    with run_server(DEFAULT_PORT) as (server, port):
        server.wait_for_termination()

if __name__ == '__main__':
    main()
