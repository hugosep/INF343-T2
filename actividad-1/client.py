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

_SERVER_ADDR_TEMPLATE = 'localhost:%d'
_SIGNATURE_HEADER_KEY = 'x-signature'
user_name = ""

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

# consulta siempre si hay mensajes para él
def listener(stub):

    while True:
        requestWaiting = stub.WaitingMsg(mensajeria_pb2.requestWaiting(user_name=user_name))
        if requestWaiting != "no msg":
            print(requestWaiting.waitingMessage)

def send_rpc(channel):

    try:
        stub = mensajeria_pb2_grpc.MensajeriaStub(channel)

        # se consulta permanentemente
        threading.Thread(target=listener, args=[stub], daemon=True).start()
        
        flag = True

        while flag:
            user_name = input("Ingresa tu nombre de usuario: ")
            response = stub.CreateUser(mensajeria_pb2.newUser(name=user_name))

            if response.response == "ok":
                flag = False
            else:
                print("Nombre de usuario no disponible, ingresar otro.")

        print("Tu nombre es: " + user_name)
        print("Con este te identificarán los demás usuarios.")

        flag = True

        while flag:
            print("Elige una opción:")
            print("1.- Chatear con un usuario")
            print("2.- Ver lista de usuarios")
            print("3.- Ver todos los mensajes enviados")
            print("4.- Salir")

            entrada = int(input(":"))

            if entrada == 1:
                chat_with = input("Chatear con: ")
                responseList = stub.ChangeReceptor(mensajeria_pb2.ToUser(receptor_name=chat_with))
                print("- Mensajes - ")

                for response in responseList:
                    print(response.user)

            elif entrada == 2:
                request = mensajeria_pb2.requestList(request=user_name)

                print("- Usuarios -")
                for user in stub.ObtainList(request):
                    print(user.name)

            elif entrada == 3:
                user = mensajeria_pb2.requestAllMsg(name=user_name)

                print("- Mensajes - ")
                for user_name in stub.ObtainAllMsg(user):
                    print(user_name.message)

            elif entrada == 4:
                return "exit"

            else:
                print("Opción no válida.")

    except grpc.RpcError as rpc_error:
        print('Error recibido: %s', rpc_error)

        print("Más corto: %s", rpc_error.debug_error_string["details"])
        return rpc_error

    else:
        print('Mensaje recibido: %s', response)
        return response


def main():
    DEFAULT_PORT = 50000

    with create_client_channel(_SERVER_ADDR_TEMPLATE % DEFAULT_PORT) as channel:
        retorno_rpc = send_rpc(channel)

        if retorno_rpc == "exit":
            return


if __name__ == '__main__':
    main()
