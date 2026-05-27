import pandas as pd
import matplotlib.pyplot as plt

# Leer archivo CSV
ventas = pd.read_csv("datos/ventas.csv")

# Crear columna total
ventas["total"] = ventas["cantidad"] * ventas["precio"]

# Calcular ventas totales
ventas_totales = ventas["total"].sum()

# Producto más vendido
producto_mas_vendido = ventas.groupby("producto")["cantidad"].sum().idxmax()

# Mostrar resultados
print("Ventas totales:", ventas_totales)
print("Producto más vendido:", producto_mas_vendido)

# Agrupar ventas por producto
ventas_por_producto = ventas.groupby("producto")["total"].sum()

# Crear gráfico
ventas_por_producto.plot(kind="bar")

# Título
plt.title("Ventas por producto")

# Guardar gráfico
plt.savefig("resultados/grafico_ventas.png")

print("Gráfico guardado correctamente")