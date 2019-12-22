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

ports = list()
names = list()
allMsgs = dict()

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

    def CreateUser(self, request, context):

        if not request.name in names:
            names.append(request.name)
            return mensajeria_pb2.responseNewUser(response = "ok")
        else:
            return mensajeria_pb2.responseNewUser(response = "repeated")
    """def MgsToUser(self, request_iterator, context):
        prev_notes = []
        for request in request_iterator:
            for response in prev_notes:
                if response.location == new_note.location:
                    yield prev_note
            prev_notes.append(request)
        return mensajeria_pb2.msgFromUser()"""

    def ChangeReceptor(self, request, context):
        receptor = request.receptor

        if receptor in names:
            return mensajeria_pb2.toUserReponse("ok")

    def ObtainList(self, request, context):
        user = request.name

        for name in names:
            yield name

    def ObtainAllMsgs(self, request, context):
        user = request.name

        for msg in allMsgs[user]:
            yield msg

@contextlib.contextmanager
def run_server(port):
    # Bind interceptor to server
    server = grpc.server(
        futures.ThreadPoolExecutor(),
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
        ports.append(port)
        logging.info("Se ha conectado un cliente.")
        yield server, port


    finally:
        server.stop(0)


def main():
    DEFAULT_PORT = 50000
    logging.info('Servidor esperando en puerto :%d', DEFAULT_PORT)
    print('Servidor esperando en puerto : ', DEFAULT_PORT)

    with run_server(DEFAULT_PORT) as (server, port):
        server.wait_for_termination()


if __name__ == '__main__':
    main()
