

def ventas():

    vendedores_con_mas_20000 = []
    vendedor_mas_vendio = None
    mes_mas_ventas = None

    perfil_vendedores = {}

    while True:
        input_choice = input("Desea ingresar datos? ")
        if input_choice.lower() == "no":
            break

        legajo = int(input("ingrese numero de legajo:"))
        nombre = input("ingrese nombre de vendedor: ")
        apellido = input("ingrese apellido de vendedor: ")
        ventas = [0] * 12
        pesos = [0] * 12

        for i in range(2):
            ventas[i] = int(input("ingrese cantidad de ventas: "))
            pesos[i] = int(input("ingrese ventas en pesos: "))

        perfil_vendedores[legajo] = {"nombre": nombre, "apellido": apellido, "ventas": ventas, "pesos": pesos}

    for legajo, detalle in perfil_vendedores.items():
        print("Legajo: " + str(legajo) + " - nombre: " + detalle["nombre"] + " - ventas: " + str(sum(ventas)))
        print(legajo, detalle)

ventas()
