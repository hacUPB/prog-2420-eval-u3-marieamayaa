def mostrar_sala(sala):
    for fila in sala:
        for asiento in fila:
            print(asiento, end=' ')  
        print() 


def reservar_asiento(sala, fila, columna):
    if sala[fila][columna] == 0:
        sala[fila][columna] = 1 
        print(f'Reserva Confirmada')
    elif sala[fila][columna] == 0:
        sala[fila][columna] = 1  
        print(f'Reserva Confirmada')
    else:
        print("Lo siento, ese asiento ya está ocupado.")


def cancelar_reserva(sala, fila, columna):
    if sala[fila][columna] == 1:
        sala[fila][columna] = 0  
        print("Reserva cancelada.")
    else:
        print("No hay reserva para cancelar en ese asiento.")

def elegir_pelicula(función):
    print('1.1. Transformers')
    print('2.1.Titanic')
    print('3.1.The Incredibles')
    función = input('Elija una pelicula:')

    if función == '1.1':
        precio=2.000
    elif función=='2.1':
        precio=1.500
    elif función=='3.1':
        precio=1.000
    else:
        print('Opción no válida')

def elegir_opcion(sala):
    print("Estado actual de la sala:")
    mostrar_sala(sala)

    print("1.2. Reservar asiento")
    print("2.2. Cancelar reserva")
    print('3.2.Mostrar sala de cine')
    opcion = input("Elija una opción: ")

    if opcion == '1.2':
        fila = int(input("Ingrese el número de fila (0-4): "))
        columna = int(input("Ingrese el número de columna (0-4): "))
        if 0 <= fila < 5 and 0 <= columna < 5:
            reservar_asiento(sala, fila, columna)  
        else:
            print("Número de fila o columna inválido.")
    elif opcion == '2.2':
        fila = int(input("Ingrese el número de fila (0-4): "))
        columna = int(input("Ingrese el número de columna (0-4): "))
        if 0 <= fila < 5 and 0 <= columna < 5:
            cancelar_reserva(sala, fila, columna)  
        else:
            print("Número de fila o columna inválido.")
    else:
        print("Opción no válida.")


def main():
    sala = [[0 for _ in range(5)] for _ in range(5)]
    
    # Llamamos a la función para mostrar las opciones
    elegir_opcion(sala)


if __name__ == "__main__":
    main()
