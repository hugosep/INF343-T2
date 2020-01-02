# Tarea 2 - Sistemas Distribuidos GRPC v/s RabbitMQ

## Actividad 1

### Ejecución
Para iniciar los servicios en los containers se deben ocupar:
* **$** ``sudo docker-compose build``
* **$** ``sudo docker-compose up server``

Se necesita levantar manualmente a los clientes:
* **$** ``sudo docker-compose run client1``
* **$** ``sudo docker-compose run client2``

### Consideraciones
* IP del servidor es ``172.20.0.10``.
* Solo se puede tener un chat activo por usuario.
* Pueden haber más de 2 usuarios.
* El asincronismo está presente en la petición y entrega de los mensajes al usuario que realice la acción, ocupando las funciones _future_ de la librería _grpc_.
* No es necesario confirmar si es que se quiere chatear con un usuario, es decir, se puede mandar un mensaje a cualquiera.
* Se creó un container especial para esta actividad que fue subido a DockerHub.
* Para ver el archivos _log.txt_ utilizar: ``tail -f log.txt`` (de igual forma se instaló _nano_ y _vim_ si le es más cómodo)

### Salida
Para salir solo basta con presionar CTRL + C. Para mayor seguridad usar el siguiente comando, una vez presionado CTRL + C:

* **$** ``sudo docker-compose down``

Para cerrar servidor: presionar CTRL + C

### Comando para crear python a partir de .proto
``python3 -m grpc_tools.protoc --proto_path=. --python_out=. --grpc_python_out=. mensajeria.proto``

### Tutorial

#### Uso general

[![Tarea 2 - Sistemas Distribuidos GRPC v/s RabbitMQ - ACT1 - Uso General](https://img.youtube.com/vi/_bDEIjysBPY/0.jpg)](https://youtu.be/_bDEIjysBPY "Tarea 2 - Sistemas Distribuidos GRPC v/s RabbitMQ - ACT1 - Uso General")

#### Registrar nuevos clientes

[![Tarea 2 - Sistemas Distribuidos GRPC v/s RabbitMQ - ACT1 - Registrar Nuevos Usuarios](http://img.youtube.com/vi/k62UYTCz3ZI/0.jpg)](https://youtu.be/k62UYTCz3ZI "Tarea 2 - Sistemas Distribuidos GRPC v/s RabbitMQ - ACT1 - Registrar Nuevos Usuarios")

