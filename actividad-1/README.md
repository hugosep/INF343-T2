# Tarea 2 - Sistemas Distribuidos GRPC v/s RabbitMQ

## Integrantes
* Camilo Núñez - 201573573-5
* Hugo Sepúlveda - 201573515-8

## Actividad 1

### Ejecución
Para iniciar los servicios en los containers se deben ocupar:
```{r, engine='bash', count_lines}
*sudo docker-compose build
*sudo docker-compose up server
```

Se necesita levantar manualmente a los clientes:
```{r, engine='bash', count_lines}
* sudo docker-compose run client1
* sudo docker-compose run client2
```
 
### Consideraciones
* IP del servidor es ```{r, engine='bash', count_lines} 172.20.0.10 ```.
* Solo se puede tener un chat activo por usuario.
* Pueden haber más de 2 usuarios.
* El asyncronismo está presente en la petición y entrega de los mensajes al usuario que realice la acción, ocupando las funciones _future_ de la librería _grpc_. 
* No es necesario confirmar si es que se quiere chatear con un usuario, es decir, se puede menada run mensaje a cualquiera.
* Para ver el archivos ```{r, engine='bash', count_lines} log.txt ``` utilizar: ```{r, engine='bash', count_lines} tail -f log.txt ``` (de igual forma se instaló __nano__ si le es más cómodo)

### Salida
Para salir solo basta con presionar CTRL + C. Para mayor seguridad usar el siguiente comando, una vez presionado CTRL + C:

```{r, engine='bash', count_lines}
sudo docker-compose down
```

Para cerrar servidor: presionar CTRL + C

### Comando para crear pyhon a partir de .proto
```{r, engine='bash', count_lines} python3 -m grpc_tools.protoc --proto_path=. --python_out=. --grpc_python_out=. mensajeria.proto```

## Tutorial

### Uso general

### Registrar nuevos clientes