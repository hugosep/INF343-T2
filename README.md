# Tarea 2 - Sistemas Distribuidos GRPC v/s RabbitMQ

## Integrantes
* Camilo Núñez - 201573573-5
* Hugo Sepúlveda - 201573515-8

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


## Actividad 2

Para ejecutar la Actividad 2, se debe crear una imagen extendida del container ``python:3``. Para ello, se debe utilizar el ``Dockerfile`` adjunto, ejecutando el comando:
```{r, engine='bash', count_lines}
docker build -t container_pika .
```

### Ejecución

Para ejecutar la aplicacion, se debe utilziar el comando:
```{r, engine='bash', count_lines}
docker-compose build && docker-compose up
```
Este deployment ejecutara 4 containers:
* ``servidor-rabbitmq``: Container que almacena al servidor de RabbitMQ.
* ``servidor-async``: Container con la app para el Chat Server.
* ``client-async-01``: Container tipo para un cliente.
* ``client-async-02``: Container tipo para un cliente.

### Ingreso:

Para ingresar al chat desde el servidor a.k.a. ``servidor-async``, se debe ir a la URL ``localhost:8888``. Una vez dentro de la página, se debe conectar al socket de comunicación, clickeando en el botón ``connect``. La conexión se iniciará con los mensajes ``connecting tows://localhost:8888/ws_channel...`` y ``Connection established``. Tras esto, se podran mandar mensajes a los canales.

Sintaxis de comando habilitados para ``servidor-async``:
* `{*canal:mensaje}`: Envia el string `mensaje` al canal `canal`.
* `{+all}`: Solicitada al servidor un lista de los canales/clientes disponibles, el servidor responde por el canal de broadcast.

Al igual que el servidor, para ingresar a un cliente del tipo ``client-async-xx`` se debe ir a la URL ``localhost:XXXX`` con `XXXX` el puerto del cliente. Por defecto, el primer cliente tiene el puerto ``8889``, el segundo cliente ``8890``, el tercer cliente ``8891`` y así sucesivamente. Una vez dentro de la página, se debe conectar al socket de comunicación, clickeando en el botón ``connect``. La conexión se iniciará con los mensajes ``connecting tows://localhost:XXXX/ws_channel...`` y ``Connection established``. Tras esto, se podran mandar mensajes a los canales.

Sintaxis de comando habilitados para ``client-async-xx``:
* `{*canal:mensaje}`: Envia el string `mensaje` al canal `canal`.
* `{**mensaje}`: Envia el string `mensaje` a todos los clientes por el canal de broadcast.
* `{+all}`: Solicitada al servidor un lista de los canales/clientes disponibles, el servidor responde por el canal de broadcast.

### Salida

Para salir solo basta con presionar CTRL + C. Para mayor seguridad usar el siguiente comando, una vez presionado CTRL + C:
```{r, engine='bash', count_lines}
docker-compose down
```

### Tutorial
#### Uso general
[![Tarea 2 - Sistemas Distribuidos GRPC v/s RabbitMQ - ACT2 - T1](http://img.youtube.com/vi/gzUZSdAUPdw/0.jpg)](https://youtu.be/gzUZSdAUPdw "Tarea 2 - Sistemas Distribuidos GRPC v/s RabbitMQ - ACT2 - T1")

#### Registrar Nuevos Clientes
[![Tarea 2 - Sistemas Distribuidos GRPC v/s RabbitMQ - ACT2 - T2](https://img.youtube.com/vi/QsxBCTbZxcs/0.jpg)](https://youtu.be/QsxBCTbZxcs "Tarea 2 - Sistemas Distribuidos GRPC v/s RabbitMQ - ACT2 - T2")

# Posible problema
En el caso de tener un conflicto por la subred creada ``ERROR: Pool overlaps with other one on this address space
``
Ocupar comando: ``docker network prune``
