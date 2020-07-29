"""
Realizar un programa que permita cargar los resultados de un torneo de fútbol. El usuario deberá ingresar la cantidad de equipos participantes y luego los nombres de dichos equipos.
Una vez hecho esto, el programa deberá presentar un menú con tres opciones:
1 – INGRESAR RESULTADOS
2- MOSTRAR POSICIONES
3- SALIR DEL PROGRAMA

	Al elegir la opción 1, el usuario ingresa los nombres de dos equipos y los goles convertidos por cada uno. El programa deberá calcular los puntos de cada equipo (3 si ganó el partido, 1 si empató y 0 si perdió) y acumular los goles a favor y en contra de cada equipo.

	Al elegir la opción 2, el programa deberá ordenar la lista de equipos por cantidad de puntos. Si hay igualdad de puntos, por diferencia de gol (Goles a favor – goles en contra). Una vez ordenada, el programa mostrará la tabla de posiciones, con las columnas Equipo, Puntos, Partidos Jugados, Goles a Favor, Goles en contra, Diferencia de gol.

	Al elegir la opción 3, se deberá indicar el equipo ganador del torneo, el equipo con más partidos jugados a favor y terminar el programa.

Utilizar la función buscar, que recibe un nombre y una lista de diccionarios. La función comparará el nombre con el campo “Nombre” de los diccionarios y devuelve la posición en la lista del nombre que coincide, o devuelve -1 si no lo encuentra. No es necesario desarrollar el código de la función.
"""


def buscar(nombre_equipo_buscado, equipos):
    for index, equipo in enumerate(equipos):
        if equipo["nombre"] == nombre_equipo_buscado:
            return index
    return -1


def torneo_de_futbol():
    cantidad_equipos = int(input("Ingrese la cantidad de equipos: "))
    equipos = []
    for i in range(cantidad_equipos):
        equipo = str(input("Ingrese el nombre de un equipo: "))
        equipos.append({"nombre": equipo, "puntos": 0, "goles_a_favor": 0, "goles_en_contra": 0, "partidos": 0})

    while True:
        menu = int(input("Seleccione la opcion 1 para ingresar resultados, 2 para mostrar posiciones y 3 para finalizar"))
        if menu == 3:
            break
        elif menu == 1:
            equipo_local = str(input("Ingrese el nombre del equipo local: "))
            goles_local = int(input("Ingrese los goles del equipo local: "))
            equipo_visitante = str(input("Ingrese el nombre del equipo visitante: "))
            goles_visitante = int(input("Ingrese los goles del equipo visitante: "))

            indice_equipo_local = buscar(equipo_local, equipos)
            indice_equipo_visitante = buscar(equipo_visitante, equipos)

            equipos[indice_equipo_local]["goles_a_favor"] = goles_local
            equipos[indice_equipo_local]["goles_en_contra"] = goles_visitante
            equipos[indice_equipo_local]["partidos"] = equipos[indice_equipo_local]["partidos"] + 1

            equipos[indice_equipo_visitante]["goles_a_favor"] = goles_visitante
            equipos[indice_equipo_visitante]["goles_en_contra"] = goles_local
            equipos[indice_equipo_visitante]["partidos"] = equipos[indice_equipo_visitante]["partidos"] + 1

            if goles_local > goles_visitante:
                equipos[indice_equipo_local]["puntos"] = equipos[indice_equipo_local]["puntos"] + 3
            elif goles_local < goles_visitante:
                equipos[indice_equipo_visitante]["puntos"] = equipos[indice_equipo_visitante]["puntos"] + 3
            else:
                equipos[indice_equipo_local]["puntos"] = equipos[indice_equipo_local]["puntos"] + 1
                equipos[indice_equipo_visitante]["puntos"] = equipos[indice_equipo_visitante]["puntos"] + 1

