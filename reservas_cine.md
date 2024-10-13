# Reservas de Movie Land
# En el trabajo se presentará un programa que permita calcular las reservas del cinema Movie Land. Esto se hará mediante una matriz nula que representara la sala de cine con respecto a sus asientos cuyas posiciones son determinadas por su respectiva fila y columna en la matriz. El usuario tendrá dos opciones, cancelar una reserva o hacer una reserva. Seguido de esto podrá elegir la función a la cual va a asistir la cual tendra asignado un número de sala cuya sala sera la matriz nula de tamaño 5x5 previamente establecida. El número de sala y la posición del asiento a elegir determinará el precio de la boleta para la función que será el dato de salida del programa confirmando la reserva de la pelicula y el precio de la misma. Al elegir la pelicula que desea ver cuya variable será asignada un número, el programá procederá a preguntar la edad del usuario para saber si puede ingresar a la función elegida, luego el usuario deberá elegir la posición del asiento que desea tomar el usuario y el programa convertira el 0 de la posición elegida en un 1 y de esta manera si se quiere hacer una nueva reserva el. 1 indica que la silla ya esta ocupada y se deberá escoger otro asiento, en caso de cancelar reserva, el 1 de la posición se convierte nuevamente en 0 y si no hay un 1 no habra reserva en este asiento para cancelar. Este programa permite entender la distribución de asientos en una sala de cine como una matriz de orden dado por las columnas y filas totales de asiento y cada posición de los asientos dados por el número de columna y el número de fila. La visualización de la sala de cine en forma de matriz es efectiva y de fácil comprensión y la asignación y manipulación de los datos de reservas se manipula de una forma más simple y organizada.

# Este programa permitirá organizar la sala de cine con una matriz cuyo tamaño (mxn)indicará la cantidad de asientos. Permitirá al usuario ingresar a una posición exacta en el asiento y el 1 y 0 permitirán que el programa evalúe la disponibilidad de la silla (1:ocupada, 0:disponible).Al evaluar la disponibilidad podrá reservar en este asiento o deberá escoger otra opción. El programá también permitirá que el usuario cancele el asiento que eligio si quiere cambiarlo o ya no desea asistir a la función.
```
Inicio
    Leer edad del usuario
    Si edad<1
        Imprimir "Edad inválida"
    Fin si

    Crear una matriz de 5x5 llamada "sala" con todos los valores en 0 

    Leer función elegir_pelicula 
    Si película no es válida=None
    Fin si

   Imprimir nombre de la película 

    Leer función elegir_asiento con la sala y la película
    Imprimir matriz actual
        
    Leer número de fila (entre 0 y 4)
    Leer número de columna (entre 0 y 4)
        
    Si fila o columna son inválidos
        Imprimir "Número de fila o columna inválido"
    Fin si
    Si asiento=0
        Reservar el asiento (cambiar el valor a 1)
        Si fila >= 3
            precio = 10,000 pesos
            Sino
                precio = 5,000 pesos
            Fin sino
        Fin si
    Fin si
                

    Imprimir "Reserva Confirmada"
    Imprimir precio 
    Imprimir película
    Imprimir fila, columna
    Imprimir nueva matriz

    Leer si desea cancelar la reserva 
    Si respuesta="si"
        columna, fila= 0
        Imprimir "Reserva cancelada"
        Imprimir matriz nueva
        Sino
            Imprimir "Lo siento, ese asiento ya está ocupado"
        Fin sino
    Fin si
Fin
```
