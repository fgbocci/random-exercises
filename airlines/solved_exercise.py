#!/usr/bin/env python
# -*- coding: utf-8 -*-

##Realizar un programa que permita registrar las ventas de pasajes para un avión. El avión tiene 28 filas de 6 asientos cada una.
##El programa deberá presentar un menú con las siguientes opciones:
##1-      Vender pasaje. Se debe mostrar un esquema de los asientos del avión indicando si están disponibles ú ocupados.
## El pasajero  puede elegir un asiento (si está libre) Si no elige, el programa debe asignarle un asiento libre.
##El pasajero indica su DNI y su edad.  El costo de los pasajes es de $1500. Los mayores de 65 años tienen un descuento del 10%.
##2-      Cerrar vuelo. El programa debe mostrar el listado de pasajeros y guardar el mismo en un archivo llamado "vuelo.txt".
##Se debe indicar además el total de pasajeros  y el porcentaje de ocupación del avión.
##3-      Finalizar. Sale del programa.


def Menu():
    print(" ")
    print("Bienvenido a Python Airlines,")
    print(" ")
    print("Por favor, escoja una opción: ")
    print(" ")
    print("Pulse (1) si desea comprar un pasaje.")
    print("Pulse (2) si desea cerrar el vuelo.")
    print("Pulse (3) si desea finalizar la compra.")
    print(" ")
    eleccionmenu = int(input("Por favor, escoja la opción: "))
    return eleccionmenu


def Descuento(i):
    if i > 65:
        costo = 1500 * 0.9
    else:
        costo = 1500
    return costo


def CompraDePasajes():
    pasajeros = []
    f = []
    for i in range(28):
        f.append([0] * 6)
    eleccionmenu = Menu()
    while eleccionmenu != 3:
        if eleccionmenu == 1:
            for i in range(0, 28):
                if i <= 28:
                    """
                    if i > -1 and i < 9:
                        print("Fila número:  ", i + 1, "----", f[i][0], f[i][1], f[i][2], f[i][3], f[i][4], f[i][5])
                    else:
                        print("Fila número: ", i + 1, "----", f[i][0], f[i][1], f[i][2], f[i][3], f[i][4], f[i][5])
                    """
                    print("Fila número:  ", i + 1, "----", f[i][0], f[i][1], f[i][2], f[i][3], f[i][4], f[i][5])
            print(
                "El esquema muestra los los asientos del avión. Un 1 indica que el asiento está ocupado, y un 0 indica que se encuentra disponible.")
            elegAsiento = str(input(
                "¿Desea elegir un asiento? (si o no) (Si elije la opción “no”, se le asignará automáticamente un asiento vacío): "))
            if elegAsiento == "si":
                Asiento = 0
                while Asiento == 0:
                    FilaEleg = int(input("Elija la fila que desea (de 1 a 28): "))
                    ColumnaEleg = int(input("Elija la hilera que desea (de 1 a 6): "))
                    if f[(FilaEleg) - 1][(ColumnaEleg) - 1] == 0:
                        print("Ha comprado el asiento en la fila: ", FilaEleg, " y en la hilera: ", ColumnaEleg)
                        Asiento = 1
                        f[(FilaEleg) - 1][(ColumnaEleg) - 1] = 1
                    else:
                        print("El asiento se encuentra ocupado, elija otro por favor")

            if elegAsiento == "no":
                Asiento2 = 0
                for i in range(0, 28):
                    for j in range(0, 6):
                        while Asiento2 == 0:
                            if f[i][j] == 0:
                                f[i][j] = 1
                                Asiento2 = 1
                                print("Ha comprado el asiento en la fila:", i + 1, "y en la hilera:", j + 1)
                            else:
                                break

            dni = int(input("Ingrese su número de DNI (sin puntos ni espacios): "))
            pasajeros.append(dni)
            edad = int(input("Ingrese su edad: "))
            print("El costo del su pasaje es de: $", Descuento(edad))
            print("------------------------------------------------------------------------------------")


        elif eleccionmenu == 2:
            print("_____________________________________________________________________________________")
            print(" ")
            print("Los DNI de los pasajeros son: ", pasajeros)
            print("El total de pasajeros es: ", len(pasajeros))
            print("El porcentaje de ocupación es: ", (len(pasajeros) / (28 * 6)) * 100, "%")
            print("_____________________________________________________________________________________")

            archivo = open("Vuelo.txt", "w")
            archivo.write('pasajeros%s' % pasajeros)
            archivo.close()

        else:
            print("por favor seleccione una opción valida")

        eleccionmenu = Menu()
    print(" ")
    print(
        "Usted ha seleccionado 3, muchísimas gracias por confiar en Python Airlines. Esperamos que haya tenido una grata experiencia!")


CompraDePasajes()
