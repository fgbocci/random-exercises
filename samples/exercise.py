
def buscar(nombre_equipo_buscado, equipos):
    for index, equipo in enumerate(equipos):
        if equipo["nombre"] == nombre_equipo_buscado:
            return index
    return -1


def ordenar_por_puntos_y_goles(equipos):
    # https://www.geeksforgeeks.org/ways-sort-list-dictionaries-values-python-using-lambda-function/
    equipos_ordenados = sorted(equipos, key=lambda equipo: (equipo["puntos"], equipo["diferencia_de_gol"]), reverse=True)
    return equipos_ordenados


def equipo_con_mas_partidos(equipos):
    equipos_ordenados_por_partidos = sorted(equipos, key=lambda equipo: (equipo["partidos"]), reverse=True)
    return equipos_ordenados_por_partidos[0]


def torneo_de_futbol():
    cantidad_equipos = int(input("Ingrese la cantidad de equipos: "))
    equipos = []
    for i in range(cantidad_equipos):
        equipo = str(input("Ingrese el nombre de un equipo: "))
        equipos.append({"nombre": equipo, "puntos": 0, "goles_a_favor": 0, "goles_en_contra": 0, "diferencia_de_gol": 0, "partidos": 0})

    while True:
        menu = int(input("Seleccione la opcion 1 para ingresar resultados, 2 para mostrar posiciones y 3 para finalizar"))
        if menu == 1:
            equipo_local = str(input("Ingrese el nombre del equipo local: "))
            goles_local = int(input("Ingrese los goles del equipo local: "))
            equipo_visitante = str(input("Ingrese el nombre del equipo visitante: "))
            goles_visitante = int(input("Ingrese los goles del equipo visitante: "))

            indice_equipo_local = buscar(equipo_local, equipos)
            indice_equipo_visitante = buscar(equipo_visitante, equipos)

            equipos[indice_equipo_local]["goles_a_favor"] = goles_local
            equipos[indice_equipo_local]["goles_en_contra"] = goles_visitante
            equipos[indice_equipo_local]["diferencia_de_gol"] = goles_local - goles_visitante
            equipos[indice_equipo_local]["partidos"] = equipos[indice_equipo_local]["partidos"] + 1

            equipos[indice_equipo_visitante]["goles_a_favor"] = goles_visitante
            equipos[indice_equipo_visitante]["goles_en_contra"] = goles_local
            equipos[indice_equipo_visitante]["diferencia_de_gol"] = goles_visitante - goles_local
            equipos[indice_equipo_visitante]["partidos"] = equipos[indice_equipo_visitante]["partidos"] + 1

            if goles_local > goles_visitante:
                equipos[indice_equipo_local]["puntos"] = equipos[indice_equipo_local]["puntos"] + 3
            elif goles_local < goles_visitante:
                equipos[indice_equipo_visitante]["puntos"] = equipos[indice_equipo_visitante]["puntos"] + 3
            else:
                equipos[indice_equipo_local]["puntos"] = equipos[indice_equipo_local]["puntos"] + 1
                equipos[indice_equipo_visitante]["puntos"] = equipos[indice_equipo_visitante]["puntos"] + 1

        elif menu == 2:
            equipos_ordenados = ordenar_por_puntos_y_goles(equipos)
            for posicion, equipo in enumerate(equipos_ordenados):
                print("Posicion: " + str(posicion + 1) + " - Equipo: " + equipo["nombre"] + " - Puntos: " + str(equipo["puntos"]) + " - Partidos jugados: " + str(equipo["partidos"]) + " - Goles a favor: " + str(equipo["goles_a_favor"]) + " - Goles en contra: " + str(equipo["goles_en_contra"]))

        elif menu == 3:
            equipos_ordenados = ordenar_por_puntos_y_goles(equipos)
            print("Equipo ganador: " + equipos_ordenados[0]["nombre"])
            equipo_mas_partidos = equipo_con_mas_partidos(equipos)
            print("Equipo con mas partidos: " + equipo_mas_partidos["nombre"])
            break


torneo_de_futbol()