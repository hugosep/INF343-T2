from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import contextlib

import grpc
import mensajeria_pb2
import mensajeria_pb2_grpc
import datetime as dt
# import _credentials
import threading
DEFAULT_IP_SERVER = "172.20.0.10"
DEFAULT_PORT = 5000

_SERVER_ADDR_TEMPLATE = '172.20.0.10:%d'
_SIGNATURE_HEADER_KEY = 'x-signature'

global user_name
user_name = ""

"""class AuthGateway(grpc.AuthMetadataPlugin):

    def __call__(self, context, callback):
        Implements authentication by passing metadata to a callback.

        Implementations of this method must not block.

        Args:
          context: An AuthMetadataContext providing information on the RPC that
            the plugin is being called to authenticate.
          callback: An AuthMetadataPluginCallback to be invoked either
            synchronously or asynchronously.
        
        # Example AuthMetadataContext object:
        # AuthMetadataContext(
        #     service_url=u'https://localhost:50051/helloworld.Greeter',
        #     method_name=u'SayHello')
        signature = context.method_name[::-1]
        callback(((_SIGNATURE_HEADER_KEY, signature),), None)"""


"""@contextlib.contextmanager
def create_client_channel(addr):
    call_credentials = grpc.metadata_call_credentials(
        AuthGateway(), name='actividad-1 gateway')

    channel_credential = grpc.ssl_channel_credentials(
        _credentials.ROOT_CERTIFICATE)

    # credencial de llamadas y channels
    composite_credentials = grpc.composite_channel_credentials(
        channel_credential,
        call_credentials,
    )
    
    channel = grpc.secure_channel(addr, composite_credentials)
    yield channel"""

# consulta siempre si hay mensajes para el
def listener(stub):

    while True:
        call_future = stub.WaitingMsg.future(mensajeria_pb2.requestUser(user_name=user_name))
        waitingMessage = call_future.result()

        if waitingMessage.message != "no msg":
            print(waitingMessage.message)

def send_rpc(channel):

    try:
        # creacion de stub
        stub = mensajeria_pb2_grpc.MensajeriaStub(channel)
        
        flag = True

        # nombre de usuario (unico)
        while flag:
            user_name = input("Ingresa tu nombre de usuario: ")
            response = stub.CreateUser(mensajeria_pb2.newUser(name=user_name))
            
            if response.response == "ok":
                flag = False
            else:
                print("Nombre de usuario no disponible, ingresar otro.")

        print("Tu nombre es: " + user_name)
        print("Con este te identificaran los demas usuarios.\n")

        flag = True

        # menu
        while flag:
            print("Elige una opcion:")
            print("1.- Enviar mensaje a usuario")
            print("2.- Ver lista de usuarios")
            print("3.- Ver todos los mensajes enviados")
            print("4.- Revisar buzon (mensajes que te han enviado)")
            print("5.- Salir")

            entrada = int(input(":"))

            if entrada == 1:
                receptor = input("Enviar mensaje a: ")
                print("(escribir \"q\" para salir)")

                while True:
                    message = input(":")

                    if message == "q":
                        break

                    call_future = stub.MsgToUser(mensajeria_pb2.msgToUser(
                        user_name=user_name,
                        receptor=receptor,
                        message=message
                        ))
                    responseCreationMsg = call_future.result()
                    
                    if responseCreationMsg.response != "ok":
                        print("Problema al enviar mensaje al servidor.")

            elif entrada == 2:
                request = mensajeria_pb2.requestList(request=user_name)

                print("-- Usuarios --")
                for user in stub.ObtainList(request):
                    print(user.nameList)
                print("")

            elif entrada == 3:
                call_future = mensajeria_pb2.requestAllMsg.future(user_name=user_name)
                user = call_future.result()
                print("-- Mensajes --")
                for responseAllMsg in stub.ObtainAllMsg(user):
                    if responseAllMsg.receptor != "-1":
                        print(str(dt.datetime.fromtimestamp(responseAllMsg.timestamp)) + " [" + responseAllMsg.receptor + "]: " + responseAllMsg.message)
                    else:
                        print("No hay mas mensajes")
                        break
                print("")

            elif entrada == 4:
                print("-- Buzon de mensajes --")
                request = mensajeria_pb2.requestMsg(user_name=user_name)

                for response in stub.ViewMsg(request):
                    print(str(dt.datetime.fromtimestamp(response.timestamp)) + " [" + response.emisor + "] : " + response.message)
                print("")

            elif entrada == 5:
                return "exit"

            else:
                print("Opcion no valida.")

    except grpc.RpcError as rpc_error:
        print('Error recibido: %s', rpc_error)
        return rpc_error

def main():
    """with create_client_channel(_SERVER_ADDR_TEMPLATE % DEFAULT_PORT) as channel:"""
    with grpc.insecure_channel(DEFAULT_IP_SERVER + ":" + str(DEFAULT_PORT)) as channel:
        retorno_rpc = send_rpc(channel)

        if retorno_rpc == "exit":
            return


if __name__ == '__main__':
    main()
