from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import contextlib

import grpc
import fibonacci_pb2
import fibonacci_pb2_grpc
import datetime as dt

DEFAULT_IP_SERVER = "172.20.0.10"
DEFAULT_PORT = 5000

_SERVER_ADDR_TEMPLATE = '172.20.0.10:%d'
_SIGNATURE_HEADER_KEY = 'x-signature'

def send_rpc(channel):

    try:
        # creacion de stub
        stub = mensajeria_pb2_grpc.MensajeriaStub(channel)
        sequence = raw(input("Request fib:"))
        responseValue = stub.CalcularFibo(fibonnacii_pb2.requestSequence(sequence=sequence))
        print("Value fib(" + str(sequence) + "): " + responseValue.value)

        return "exit"

    except grpc.RpcError as rpc_error:
        print('Error recibido: %s', rpc_error)
        return rpc_error

def main():
    
    with grpc.insecure_channel(DEFAULT_IP_SERVER + ":" + str(DEFAULT_PORT)) as channel:
        retorno_rpc = send_rpc(channel)

        if retorno_rpc == "exit":
            return


if __name__ == '__main__':
    main()
