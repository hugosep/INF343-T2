from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import contextlib
import logging

import grpc
import mensajeria_pb2
import mensajeria_pb2_grpc
import _credentials
import threading

_LOGGER = logging.getLogger(__name__)
_LOGGER.setLevel(logging.INFO)

_SERVER_ADDR_TEMPLATE = '172.20.0.10:%d'
_SIGNATURE_HEADER_KEY = 'x-signature'
user_name = ""
historial = list()

class AuthGateway(grpc.AuthMetadataPlugin):

    def __call__(self, context, callback):
        """Implements authentication by passing metadata to a callback.

        Implementations of this method must not block.

        Args:
          context: An AuthMetadataContext providing information on the RPC that
            the plugin is being called to authenticate.
          callback: An AuthMetadataPluginCallback to be invoked either
            synchronously or asynchronously.
        """
        # Example AuthMetadataContext object:
        # AuthMetadataContext(
        #     service_url=u'https://localhost:50051/helloworld.Greeter',
        #     method_name=u'SayHello')
        signature = context.method_name[::-1]
        callback(((_SIGNATURE_HEADER_KEY, signature),), None)


@contextlib.contextmanager
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
    yield channel

# consulta siempre si hay mensajes para el
def listener(stub):

    while True:
        call_future = stub.WaitingMsg.future(mensajeria_pb2.requestUser(user_name=user_name))
        waitingMessage = call_future.result()

        if waitingMessage.message != "no msg":
            print(waitingMessage.message)

def send_rpc(channel):

    try:
        stub = mensajeria_pb2_grpc.MensajeriaStub(channel)
        
        flag = True

        while flag:
            user_name = input("Ingresa tu nombre de usuario: ")
            response = stub.CreateUser(mensajeria_pb2.newUser(name=user_name))
            #threading.Thread(target=listener, args=[stub], daemon=True).start()
            
            if response.response == "ok":
                flag = False
            else:
                print("Nombre de usuario no disponible, ingresar otro.")

        print("Tu nombre es: " + user_name)
        print("Con este te identificaran los demas usuarios.\n")

        flag = True

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
                while True:
                    message = input("(q para salir):")

                    if message == "q":
                        break

                    responseCreationMsg = stub.MsgToUser(mensajeria_pb2.msgToUser(
                        user_name=user_name,
                        receptor=receptor,
                        message=message
                        ))

                    if responseCreationMsg.response != "ok":
                        print("Problema al enviar mensaje al servidor.")

            elif entrada == 2:
                request = mensajeria_pb2.requestList(request=user_name)

                print("-- Usuarios --")
                for user in stub.ObtainList(request):
                    print(user.nameList)
                print("")

            elif entrada == 3:
                user = mensajeria_pb2.requestAllMsg(user_name=user_name)

                print("-- Mensajes --")
                for responseAllMsg in stub.ObtainAllMsg(user):
                    if responseAllMsg.receptor != "-1":
                        print("[" + responseAllMsg.receptor + "]: " + responseAllMsg.message)
                    else:
                        print("No hay mas mensajes")
                        break
                print("")

            elif entrada == 4:
                print("-- Buzon de mensajes --")
                request = mensajeria_pb2.requestMsg(user_name=user_name)

                for response in stub.ViewMsg(request):
                    print("[" + response.emisor + "] : " + response.message)
                print("")

            elif entrada == 5:
                return "exit"

            else:
                print("Opcion no valida.")

    except grpc.RpcError as rpc_error:
        print('Error recibido: %s', rpc_error)
        return rpc_error

def main():
    DEFAULT_PORT = 5000

    """with create_client_channel(_SERVER_ADDR_TEMPLATE % DEFAULT_PORT) as channel:"""
    with grpc.insecure_channel('172.20.0.10:5000') as channel:
        retorno_rpc = send_rpc(channel)

        if retorno_rpc == "exit":
            return


if __name__ == '__main__':
    main()
