## Objetivo

El objetivo de este proyecto es desarrollar un sistema que permita gestionar viajes de forma ordenada, incluyendo la administración de destinos, pasajeros y reservas.

Se busca facilitar el manejo de la información, reducir errores y mantener un control claro sobre la disponibilidad de cupos y las reservas realizadas, aplicando los contenidos vistos en la materia.


## Alcance del sistema

El sistema cubrirá las funcionalidades básicas necesarias para la gestión de viajes:

* Carga de nuevos viajes
* Registro de pasajeros
* Creación de reservas
* Cancelación de reservas
* Consulta de viajes disponibles
* Consulta de pasajeros registrados
* Control de cupos por viaje
* Visualización de pasajeros por viaje


## Funcionalidades principales

### Carga de viajes

Permite registrar viajes con información como destino, fecha, precio y cantidad de cupos disponibles. Cada viaje cuenta con un identificador único.

### Registro de pasajeros

Permite almacenar datos de pasajeros como DNI, nombre, apellido y contacto.

### Gestión de reservas

Permite asignar un pasajero a un viaje si hay disponibilidad. En caso contrario, el sistema informa que no hay cupos.

### Consulta de viajes

Permite visualizar todos los viajes cargados junto con su información y disponibilidad.

### Cancelación de reservas

Permite eliminar una reserva existente y actualizar automáticamente los cupos disponibles.

### Visualización de información

Permite generar listados como:

* viajes con disponibilidad
* viajes completos
* pasajeros por viaje


## Flujo de funcionamiento

1. Se cargan los viajes en el sistema
2. Se registran los pasajeros
3. Se realizan reservas según disponibilidad
4. Se pueden consultar los datos en cualquier momento
5. En caso de cancelación, se actualizan automáticamente los cupos


## Estructura del sistema

El sistema estará organizado en funciones, cada una encargada de una tarea específica:

* Gestión de viajes
* Gestión de pasajeros
* Gestión de reservas
* Visualización de datos

Se utilizarán estructuras como listas y diccionarios para almacenar la información.
El código se organizará de forma clara para facilitar su comprensión y mantenimiento.


## Resultado esperado

Se espera obtener un sistema que permita:

* Conocer los viajes disponibles
* Ver la cantidad de cupos de cada viaje
* Consultar los pasajeros registrados
* Controlar las reservas realizadas

El sistema debe facilitar la gestión general y minimizar errores en la administración de datos.

## Avance del proyecto (40%)

Para la primera entrega se desarrollará una versión inicial que incluya:

* Registro de viajes
* Registro de pasajeros
* Reservas básicas
* Consulta de disponibilidad
* Visualización de datos

El código estará estructurado en funciones para permitir una evolución progresiva del sistema.
