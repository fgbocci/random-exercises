
# Variables de control
monto_variacion_comision = 10000
comision_minima = 100
vendedores_especiales = [8129, 3299, 4502]


# Calculo de comision
def comision(codigo_vendedor, ventas_totales):

    comision = 0

    if ventas_totales > monto_variacion_comision:
        if codigo_vendedor in vendedores_especiales:
            comision = 0.07 * ventas_totales
        else:
            comision = 0.06 * ventas_totales
    elif ventas_totales <= monto_variacion_comision:
        comision = 0.05 * ventas_totales

    comision = max(comision, comision_minima)

    return comision


def reporte_de_comisiones():

    vendedor_que_mas_vendio = 0
    ventas_vendedor_que_mas_vendio = 0

    vendedores_hombres = 0
    comision_vendedores_hombres = 0

    vendedores_mujeres = 0
    comision_vendedores_mujeres = 0

    while True:
        codigo_vendedor = int(input("Ingrese el codigo de vendedor o 0 para terminar: "))

        if codigo_vendedor == 0:
            break

        genero_vendedor = str(input("Ingrese el genero del vendedor: "))
        total_vendido_vendedor = int(input("Ingrese el total vendido por el vendedor: "))
        comision_vendedor = comision(codigo_vendedor, total_vendido_vendedor)
        print("Comision de " + str(codigo_vendedor) + ": " + str(comision_vendedor))

        if genero_vendedor == "M":
            vendedores_hombres += 1
            comision_vendedores_hombres += comision_vendedor
        else:
            vendedores_mujeres += 1
            comision_vendedores_mujeres += comision_vendedor

        if total_vendido_vendedor > ventas_vendedor_que_mas_vendio:
            vendedor_que_mas_vendio = codigo_vendedor
            ventas_vendedor_que_mas_vendio = total_vendido_vendedor

    print("El vendedor que mas vendio fue " + str(vendedor_que_mas_vendio) + " y vendio $" + str(ventas_vendedor_que_mas_vendio))
    if vendedores_hombres > 0:
        print("El promedio de ventas entre hombres fue de: " + str(float(comision_vendedores_hombres) / float(vendedores_hombres)))
    else:
        print("No hubo vendedores hombres - no se muestra el promedio de ventas para vendedores hombres")

    if vendedores_mujeres > 0:
        print("El promedio de ventas entre mujeres fue de: " + str(float(comision_vendedores_mujeres) / float(vendedores_mujeres)))
    else:
        print("No hubo vendedores mujeres - no se muestra el promedio de ventas para vendedores mujeres")

    print("El total de comisiones a pagar es de: $" + str(comision_vendedores_hombres + comision_vendedores_mujeres))


reporte_de_comisiones()
