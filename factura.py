#Solicita nombre del producto, precio y cantidad. Calcula el subtotal y muestra un resumen de la compra.

nombreProducto = input("Producto: ")
precioProducto = int(input("Precio: C$"))
cantidadProducto = int(input("Cantidad: "))
subTotal = precioProducto * cantidadProducto
Total = subTotal * 1.15
#El 1.15 es valor de IVA (15%)
print(" ----    ----    ----    ----    ----")
print("              RESUMEN                ")
print(" ----    ----    ----    ----    ----")

print(nombreProducto)
print("SUBTOTAL: C$" + str(subTotal))
print("TOTAL: C$" + str(Total))