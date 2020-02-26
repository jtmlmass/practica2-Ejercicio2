cantidad = 100
cantidad += 1
cantidad_cestas = cantidad
cantidad_productos = cantidad
# Productos pertenecientes a cada cesta
cestas = [[] for x in range(cantidad_cestas)]
# Cestas pertenecientes a cada producto
productos = [[] for x in range(cantidad_productos)]
cantidad_aparicion_producto = [0 for x in range(cantidad_productos)]

# Esta parte inserta los productos en sus cestas correspondientes
for cesta in range(cantidad_cestas):
    for producto in range(cantidad_productos):
        # La clave de que cesta va a cada una es que debe ser modulo == 0 la cantidad de Cesta con Producto
        if producto > 0 and producto <= cesta and cesta % producto == 0:
            cestas[cesta].append(producto)

# Esta parte es para imprimir las cestas con sus items
for cesta in range(len(cestas)):
    if cesta > 0:
        print("Cesta " + str(cesta) + ": " + str(cestas[cesta]))

for producto in range(cantidad_productos):
    for cesta in range(cantidad_cestas):
        if producto > 0 and producto <= cesta and cesta % producto == 0:
            productos[producto].append(cesta)
            cantidad_aparicion_producto[producto] += 1

for producto in range(len(productos)):
    if producto > 0:
        print("Producto " + str(producto) + ": " + str(productos[producto]))

# Cantidad de Cestas con al menos 5 productos
# soporte_minimo = 5
# cestas_soporte_minimo = []
# for cesta in range(cantidad_cestas):
#     if len(cestas[cesta]) >= soporte_minimo:
#         cestas_soporte_minimo.append(cestas[cesta])

# for cesta in range(len(cestas_soporte_minimo)):
#     print("Cesta " + str(cestas_soporte_minimo[cesta][len(
#         cestas_soporte_minimo[cesta])-1]) + ": " + str(cestas_soporte_minimo[cesta]))

# print("La Cantidad de productos frecuentes con un Soporte Mínimo de " +
#       str(soporte_minimo) + " es " + str(len(cestas_soporte_minimo)))

# Pregunta 1.2.1: Si el soporte mínimo es de 5, ¿Cuáles productos son frecuentes?
print("\nPregunta 1.2.1:")
soporte_minimo = 5
productos_soporte_minimo = []
for producto in range(cantidad_productos):
    if len(productos[producto]) >= soporte_minimo:
        productos_soporte_minimo.append(productos[producto])

for producto in range(len(productos_soporte_minimo)):
    print("Producto " + str(productos_soporte_minimo[producto][0]) + ": " + str(
        productos_soporte_minimo[producto]))

print("La Cantidad de productos frecuentes con un Soporte Mínimo de " +
      str(soporte_minimo) + " es " + str(len(productos_soporte_minimo)))

# 1.2.2. Si el soporte mínimo es de 5 ¿Cuáles pares de productos son frecuentes?
print("\nPregunta 1.2.2:")
# for producto in range(len(cantidad_aparicion_producto)):
#     if producto > 0:
#         print("Producto " + str(producto) + ": " +
#               str(cantidad_aparicion_producto[producto]))

# Estos son dos arreglos paralelos con los pares y su cantidad de aparición
pares_productos_cestas = []  # Por motivo de simplificación, esto es PPC
cantidad_ppc = []

for id_cesta in range(len(productos_soporte_minimo)):
    cesta = productos_soporte_minimo[id_cesta]
    for id_producto_1 in range(len(cesta)):
        for id_producto_2 in range(len(cesta)):
            par_productos = [cesta[id_producto_1], cesta[id_producto_2]]
            if(par_productos[0] != par_productos[1]) and par_productos not in pares_productos_cestas:
                pares_productos_cestas.append(par_productos)

cantidad_ppc = [0 for par in range(len(pares_productos_cestas))]
for id_par in range(len(pares_productos_cestas)):
    for cesta in cestas:
        if list(set(cesta).intersection(pares_productos_cestas[id_par])) == pares_productos_cestas[id_par]:
            cantidad_ppc[id_par] += 1

for par in range(len(pares_productos_cestas)):
    if cantidad_ppc[par] > soporte_minimo:
        print(str(pares_productos_cestas[par]) +
              ": " + str(cantidad_ppc[par]) + ", ", end="")

# 1.2.3.¿Cuánto da la suma de los tamaños de todas las cestas?
print("\nPregunta 1.2.3:")
total_tamaños_cestas = 0
for cesta in cestas:
    total_tamaños_cestas += len(cesta)

print("El total de los tamaños de todas las cestas es: " + str(total_tamaños_cestas))
