# Tarea 2 - Sistemas Distribuidos GRPC v/s RabbitMQ

## Integrantes
* Camilo Núñez - 201573573-5
* Hugo Sepúlveda - 201573515-8
 
## Actividad 2

Para ejecutar la Actividad 2, se debe crear una imagen extendida del container ``python:3``. Para ello, se debe utilizar el ``Dockerfile`` adjunto, ejecutando el comando:
```{r, engine='bash', count_lines}
docker build -t container_pika .
```

### Ejecuación

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
* aaaaaa

Al igual que el servidor, para ingresar a un cliente del tipo ``client-async-xx`` se debe ir a la URL ``localhost:XXXX`` con `XXXX` el puerto del cliente. Por defecto, el primer cliente tiene el puerto ``8889``, el segundo cliente ``8890``, el tercer cliente ``8891`` y así sucesivamente. Una vez dentro de la página, se debe conectar al socket de comunicación, clickeando en el botón ``connect``. La conexión se iniciará con los mensajes ``connecting tows://localhost:XXXX/ws_channel...`` y ``Connection established``. Tras esto, se podran mandar mensajes a los canales.

Sintaxis de comando habilitados para ``client-async-xx``:
* aaaaaa

## Salida

Para salir solo basta con presionar CTRL + C. Para mayor seguridad usar el siguiente comando, una vez presionado CTRL + C:
```{r, engine='bash', count_lines}
docker build -t container_pika .
```