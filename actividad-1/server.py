# Copyright 2019 The gRPC Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Server of the Python example of customizing authentication mechanism."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import argparse
import contextlib
import logging
from concurrent import futures

import grpc
import mensajeria_pb2
import mensajeria_pb2_grpc
import _credentials

logging.basicConfig(level = logging.INFO, filename = 'log.txt', filemode = 'w', format = '%(asctime)s - %(message)s')

_LISTEN_ADDRESS_TEMPLATE = 'localhost:%d'
_SIGNATURE_HEADER_KEY = 'x-signature'

ports = dict()
names = list()
# tendrá como llave el nombre del usuario al que le llega un mensaje y como value
# otro diccionario con la llave el nombre de quien lo envía y value el mensaje
allMsgs = dict()
chats = dict()
port = 0
user_name = ""

class SignatureValidationInterceptor(grpc.ServerInterceptor):

    def __init__(self):

        def abort(ignored_request, context):
            context.abort(grpc.StatusCode.UNAUTHENTICATED, 'Firma invalida')

        self._abortion = grpc.unary_unary_rpc_method_handler(abort)

    def intercept_service(self, continuation, handler_call_details):
        # Example HandlerCallDetails object:
        #     _HandlerCallDetails(
        #       method=u'/helloworld.Greeter/SayHello',
        #       invocation_metadata=...)
        method_name = handler_call_details.method.split('/')[-1]
        expected_metadata = (_SIGNATURE_HEADER_KEY, method_name[::-1])
        if expected_metadata in handler_call_details.invocation_metadata:
            return continuation(handler_call_details)
        else:
            return self._abortion


class Mensajeria(mensajeria_pb2_grpc.MensajeriaServicer):

    # avisa si hay mensajes para un determinado usuario, y lo envía en caso de haberlo
    def WaitingMsg(self, request, context):

        # hay mensajes
        if allMsgs[request.user_name] != []:
            user, msg = allMsgs[request.user_name][-1].items()
            return mensajeria_pb2.responseWaiting(message=user + ":" + msg)

        return mensajeria_pb2.responseWaiting(message="no msg")

    # crea usuario
    def CreateUser(self, request, context):
        user_name = request.name

        if not user_name in names:
            names.append(user_name)
            allMsgs[user_name] = list()
            return mensajeria_pb2.responseNewUser(response="ok")
        else:
            return mensajeria_pb2.responseNewUser(response="repeated")

    # envia mensaje entre usuarios
    def MgsToUser(self, request_iterator, context):
        
        for msgFromUser in request_iterator:
            msg = msgFromUser.response
            new_msg = mensajeria_pb2.MsgToUser(send(msg))
            yield new_msg

    # cambiar receptor de los mensajes
    def ChangeReceptor(self, request, context):
        receptor = request.receptor
        emisor = request.receptor
        
        if receptor in names:
            chats[emisor] = receptor
            return mensajeria_pb2.ToUserResponse("ok")
        else:
            return mensajeria_pb2.ToUserResponse("problem")

    # envia lista de todos los usuarios
    def ObtainList(self, request, context):
        user_name = request.request
        
        if user_name in names:
            for name in names:
                name = mensajeria_pb2.responseList(name=name)
                yield name

    # envia todos los mensajes que ha enviado el usuario que la pide
    def ObtainAllMsg(self, request, context):
        user = request.name

        for msg in allMsgs[user]:
            yield msg

@contextlib.contextmanager
def run_server(port):
    # Bind interceptor to server
    print("en run_server")

    server = grpc.server(
        futures.ThreadPoolExecutor(),
        #handlers=[hello_handler],
        interceptors=(SignatureValidationInterceptor(),))

    mensajeria_pb2_grpc.add_MensajeriaServicer_to_server(Mensajeria(), server)

    # Loading credentials
    server_credentials = grpc.ssl_server_credentials(((
        _credentials.SERVER_CERTIFICATE_KEY,
        _credentials.SERVER_CERTIFICATE,
    ),))

    # Pass down credentials
    port = server.add_secure_port(_LISTEN_ADDRESS_TEMPLATE % port,
                                  server_credentials)
    server.start()

    try:
        yield server, port

    finally:
        server.stop(0)

"""class hello_handler(grpc.GenericRpcHandler):
    
    def __init__(self):
        print("hello, new client")
        pass"""

def main():
    DEFAULT_PORT = 50000
    logging.info('Servidor esperando en puerto :%d', DEFAULT_PORT)
    print('Servidor esperando en puerto : ', DEFAULT_PORT)
    cant_clientes = 0

    with run_server(DEFAULT_PORT) as (server, port):
        print("en with")
        cant_clientes += 1
        logging.info("Se ha conectado un cliente, ID " + str(cant_clientes))
        print("Se ha conectado un cliente, ID " + str(cant_clientes))

        server.wait_for_termination()
        print(user_name)
if __name__ == '__main__':
    main()
