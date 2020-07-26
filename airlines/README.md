## Reglas

### Menu

```python
selected_choice = int(input("Ingresa la opcion: "))
```

Te pide un ingreso por teclado y guarda el valor en `selected_choice`


### Repetir una accion, al menos una vez

**Ejemplo**: pedir al usuario que ingrese un valor. Si el valor es `3`, terminar la ejecucion

```python
while True:
    selected_choice = int(input("Ingresa la opcion: "))
    if selected_choice == 3:
        break
    ...
```

### Escribir en un archivo

```python
contenido_a_escribir = ["1", "2", "3"]

with open("nombre_de_archivo.txt", "w+") as f:
    f.write(str(contenido_a_escribir))
```

### Inicializar una matriz

```python
matrix = []
n_filas = 28
n_columnas = 6
for i in range(n_filas):
    matrix.append([0] * n_columnas)  # Is the same than plane.append([0, 0, 0, 0, 0, 0])

return matrix
```

> Imaginemos que nos piden que el usuario ingrese la cantidad de filas y de columnas

```python
matrix = []
n_filas = int(input("Numero de filas: "))
n_columnas = int(input("Numero de columnas: "))
# Si lo quisiera imprimir
print(n_filas)
print(n_columnas)
for i in range(n_filas):
    matrix.append([0] * n_columnas)  # Is the same than plane.append([0, 0, 0, 0, 0, 0])

return matrix
```
