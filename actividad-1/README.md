# Actividad 2


* Solo se puede tener un chat activo por usuario.
* Pueden haber más de 2 usuarios.
* Es necesario confirmar si es que se quiere chatear con un usuario.
* Mensajes serán imprimirdos en terminal automáticamente, pudiendo afectar la visibilidad del menú.

# Comando para crear pyhon a partir de .proto
python3 -m grpc_tools.protoc --proto_path=. --python_out=. --grpc_python_out=. mensajeria.proto