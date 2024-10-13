def mostrar_sala(sala):
    for fila in sala:
        for asiento in fila:
            print(asiento, end=' ')
        print()

def reservar_asiento(sala, fila, columna):
    if sala[fila][columna] == 0:
        sala[fila][columna] = 1  # Reservar el asiento según posición en la matriz
        if fila >= 3:
            precio = 10000
        else:
            precio = 5000
        print(f'Reserva Confirmada. El precio de su asiento es {precio} pesos.')
        return precio, sala
    else:
        print("Lo siento, ese asiento ya está ocupado.")
        return None, sala

def cancelar_reserva(sala, fila, columna):
    if sala[fila][columna] == 1:
        sala[fila][columna] = 0  # Cancelar la reserva de un 1 a un 0
        print("Reserva cancelada.")
        return sala
    else:
        print("No hay reserva para cancelar en ese asiento.")
        return sala

def elegir_pelicula(edad):
    print('1.1. Transformers')
    print('2.1. Titanic')
    print('3.1. The Incredibles')
    print('4.1. IT (Restricción de edad)')

    función = input('Elija el número de la película: (1.1, 2.1, 3.1, 4.1) ')

    if función == '1.1':
        return "Transformers"
    elif función == '2.1':
        return "Titanic"
    elif función == '3.1':
        return "The Incredibles"
    elif función == '4.1':
        if edad < 16:
            print("Lo siento, no puedes ver 'IT'.")
            return None
        else:
            return "IT"
    else:
        print('Opción no válida')
        return None

def elegir_asiento(sala, película):
    print("Estado actual de la sala:")
    mostrar_sala(sala)

    fila = int(input("Ingrese el número de fila (0-4): "))
    columna = int(input("Ingrese el número de columna (0-4): "))
    
    if 0 <= fila < 5 and 0 <= columna < 5:
        precio, sala = reservar_asiento(sala, fila, columna)
        if precio is not None:
            print(f"Resumen de la reserva:")
            print(f"Película: {película}")
            print(f"Asiento: Fila {fila + 1}, Columna {columna + 1}")
            print(f"Precio: {precio} pesos")
            print("Sala actualizada:")
            mostrar_sala(sala)
            
            # Opción para cancelar la reserva
            cancelar = input("¿Desea cancelar su reserva? (si/no): ").lower()
            if cancelar == 'si':
                sala = cancelar_reserva(sala, fila, columna)
                print("Sala después de la cancelación:")
                mostrar_sala(sala)
        else:
            print("No se pudo completar la reserva.")
    else:
        print("Número de fila o columna inválido.")

def main():
    edad = int(input("Ingrese su edad: "))
    
    if edad < 1:
        print("Edad inválida.")
        return
    
    sala = [[0 for _ in range(5)] for _ in range(5)]
    
    película = elegir_pelicula(edad)
    
    if película:  # Si se eligió una película válida
        print(f"Has elegido ver {película}.")
        elegir_asiento(sala, película)

if __name__ == "__main__":
    main()


