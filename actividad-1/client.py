from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import contextlib
import logging

import grpc
import mensajeria_pb2
import mensajeria_pb2_grpc
import _credentials

_LOGGER = logging.getLogger(__name__)
_LOGGER.setLevel(logging.INFO)

_SERVER_ADDR_TEMPLATE = 'localhost:%d'
_SIGNATURE_HEADER_KEY = 'x-signature'


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
    # Call credential object will be invoked for every single RPC
    call_credentials = grpc.metadata_call_credentials(
        AuthGateway(), name='actividad-1 gateway')

    # Channel credential will be valid for the entire channel
    channel_credential = grpc.ssl_channel_credentials(
        _credentials.ROOT_CERTIFICATE)

    # Combining channel credentials and call credentials together
    composite_credentials = grpc.composite_channel_credentials(
        channel_credential,
        call_credentials,
    )
    channel = grpc.secure_channel(addr, composite_credentials)
    yield channel


def send_rpc(channel):
    stub = mensajeria_pb2_grpc.MensajeriaStub(channel)

    print("Conectado.")

    try:
        flag = True

        while flag:
            print("Ingresa tu nombre de usuario: ")
            user_name = input()
            response = stub.CreateUser(mensajeria_pb2.newUser(name=user_name))

            if response.response == "ok":
                flag = False
            else:
                print("Nombre de usuario no disponible, ingresar otro.")

        print("Tu nombres es: "+ user_name + ", con este te identificaran los demas usuarios")

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
                response = stub.ChangeReceptor(mensajeria_pb2.toUser(receptor_name=receptor_user))
                print("- Mensajes - ")

                for user_name in responseList:
                    print(response.user)

            elif entrada == 2:
                response = stub.ObtainList(mensajeria_pb2.requestList(request=user_name))
                print("- Usuarios -")
                
                for msg in response:
                    print(msg)

            elif entrada == 3:

                responseAllMsg = stub.ObtainAllMsg(mensajeria_pb2.requestAllMsg(receptor_name=receptor_user))
                print("- Mensajes - ")

                for user_name in responseAllMsg:
                    print(user_name.user)

            elif entrada == 4:
                return "exit"

            else:
                print("Opcion no valida")

    except grpc.RpcError as rpc_error:
        print('Error recibido: %s', rpc_error)
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
