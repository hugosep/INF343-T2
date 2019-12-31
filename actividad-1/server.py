from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import argparse
import contextlib
import logging
from concurrent import futures
import datetime as dt

import grpc
import mensajeria_pb2
import mensajeria_pb2_grpc
import _credentials

# creacion log.txt
logging.basicConfig(level = logging.INFO, filename = 'log.txt', filemode = 'w', format = '%(asctime)s - %(message)s')

# strings para definir servidor
_LISTEN_ADDRESS_TEMPLATE = '[::]:%d'
_SIGNATURE_HEADER_KEY = 'x-signature'
DEFAULT_PORT = 5000

# nombres
names = list()

# tendra como llave el nombre del usuario al que le llega un mensaje y como value
# otro diccionario con la llave el nombre de quien lo envia y value el mensaje
allMsgs = dict()
id_user = dict()
id_msg = dict()
port = 0
user_name = ""

cant_clientes = 0
cant_mensajes = 0
# tendra como llave el usuario emisor, donde el value seraun diccionario con el
# receptor como llave y value el mensaje
reverseAllMsgs = dict()


class NewUser(grpc.ServerInterceptor):
    def intercept_service(self, continuation, handler_call_details):
        logging.info("Se ha conectado un cliente, ID " + str(cant_clientes))
        return continuation(handler_call_details)

"""class SignatureValidationInterceptor(grpc.ServerInterceptor):

    def __init__(self):

        def abort(ignored_request, context):
            context.abort(grpc.StatusCode.UNAUTHENTICATED, 'Firma invalida')
        logging.info("Se ha conectado un cliente, ID " + str(cant_clientes))
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
            return self._abortion"""


class Mensajeria(mensajeria_pb2_grpc.MensajeriaServicer):

    # avisa si hay mensajes para un determinado usuario, y lo envia en caso de haberlo
    def WaitingMsg(self, request, context):

        # si hay mensajes
        if allMsgs[request.user_name] != []:
            user, msg = allMsgs[request.user_name][-1].items()
            allMsgs[request.user_name].pop(-1)
            return mensajeria_pb2.waitingMessage(message=user + ": " + msg)
        # sino
        return mensajeria_pb2.waitingMessage(message="no msg")

    # crea usuario
    def CreateUser(self, request, context):
        user_name = request.name

        if not user_name in names:
            names.append(user_name)
            allMsgs[user_name] = list()
            reverseAllMsgs[user_name] = list()
            global cant_clientes
            cant_clientes += 1
            id_user[cant_clientes] = user_name
            logging.info("Nuevo usuario: nombre, " + user_name + ", ID: " + str(cant_clientes))
            return mensajeria_pb2.responseNewUser(response="ok")
        else:
            return mensajeria_pb2.responseNewUser(response="repeated")

    # envia mensaje entre usuarios
    def MsgToUser(self, request, context):
        global cant_mensajes
        cant_mensajes += 1
        
        ahora = dt.datetime.now()
        id_msg[cant_mensajes] = [request.message, dt.datetime.timestamp(ahora)]
        
        logging.info(str(ahora) + "[" + request.user_name + "] a [" + request.receptor + "], mensaje:" + request.message + ", ID: " + str(cant_mensajes))
        allMsgs[request.receptor].append(dict({request.user_name : cant_mensajes}))
        reverseAllMsgs[request.user_name].append(dict({request.receptor : cant_mensajes}))
        
        return mensajeria_pb2.responseCreationMsg(response="ok")

    # envia lista de todos los usuarios
    def ObtainList(self, request, context):
        user_name = request.request
        
        if user_name in names:
            for name in names:
                name = mensajeria_pb2.responseList(nameList=name)
                yield name

    # manda mensajes que se le han enviado
    def ViewMsg(self, request, context):
        diccionarios = allMsgs[request.user_name]
        
        for msg in diccionarios:
            emisor = list(msg.keys())[0]
            message = id_msg[list(msg.values())[0]][0]
            timestamp = id_msg[list(msg.values())[0]][1]

            yield mensajeria_pb2.responseMsg(
                emisor=emisor,
                message=message,
                timestamp=timestamp
                )

    # envia todos los mensajes que ha enviado el usuario que la pide
    def ObtainAllMsg(self, request, context):
        user_name = request.user_name
        if reverseAllMsgs[user_name]:

            msgs = reverseAllMsgs[user_name]
            
            for msg in msgs:
                receptor = list(msg.keys())[0]
                id_message = list(msg.values())[0]

                yield mensajeria_pb2.responseAllMsg(
                    receptor=receptor,
                    message=id_msg[id_message][0],
                    timestamp=id_msg[id_message][1]
                    )
        else:
            return mensajeria_pb2.responseAllMsg(
                    receptor="-1",
                    message="-1"
                    )

@contextlib.contextmanager
def run_server(port):

    server = grpc.server(
        futures.ThreadPoolExecutor())
        #interceptors=(NewUser(),))
        #handlers=[hello_handler],
        #interceptors=(SignatureValidationInterceptor(),))

    mensajeria_pb2_grpc.add_MensajeriaServicer_to_server(Mensajeria(), server)

    # Loading credentials
    """server_credentials = grpc.ssl_server_credentials(((
        _credentials.SERVER_CERTIFICATE_KEY,
        _credentials.SERVER_CERTIFICATE,
    ),))

    # Pass down credentials
    port = server.add_secure_port(_LISTEN_ADDRESS_TEMPLATE % port,
                                  server_credentials)"""

    server.add_insecure_port(_LISTEN_ADDRESS_TEMPLATE % port)
    print('Servidor esperando en puerto :%d', DEFAULT_PORT)
    logging.info('Servidor esperando en puerto :%d', DEFAULT_PORT)
    server.start()

    try:
        yield server, port

    finally:
        server.stop(0)

def main():
    cant_clientes = 0
    with run_server(DEFAULT_PORT) as (server, port):
        server.wait_for_termination()

if __name__ == '__main__':
    main()
