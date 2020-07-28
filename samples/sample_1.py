def padrones():

    alumnos = {}
    materias_aprobadas_por_todos = set()

    while True:
        padron = int(input("ingrese su numero de padron(ingrese -1 para terminar):"))
        if padron < 0:
            break

        materias_aprobadas = set()

        Numero_materias = int(input("ingrese el numero de materias aprobadas:"))
        for i in range(0, Numero_materias):
            codigo_materia = int(input("ingrese el codigo de materia:"))
            if codigo_materia <= 0:
                print("error, codigo no valido")
                codigo_materia = int(input("ingrese un codigo valido de materia:"))
            else:
                materias_aprobadas.add(codigo_materia)
                materias_aprobadas_por_todos.add(codigo_materia)

            alumnos[padron] = len(materias_aprobadas)

    for alumno, materias in alumnos.items():
        print("Alumno " + str(alumno) + " aprobo " + str(materias) + " materias")

    print("Materias aprobadas por al menos 1 alumno: " + str(materias_aprobadas_por_todos))


padrones()
