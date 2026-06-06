from google.colab import drive
drive.mount('/content/drive')
%cd /content/drive/MyDrive/Colab Notebooks/TP Intengrador/AnalisisDeVentas

import csv
from datetime import datetime

# ---------------------------------------------------------
# Cargar ventas desde el archivo CSV
# ---------------------------------------------------------
def cargar_ventas():
    ventas = []  # creo la variable ventas, usando una tabla

    with open("/content/drive/MyDrive/Colab Notebooks/TP Intengrador/AnalisisDeVentas/sales_sample_2024.csv",
              "r", encoding="utf-8") as archivo:  # abro el archivo en modo lectura

        lector = csv.DictReader(archivo)
        for fila in lector:  # utilizo un for para que recorra todos los valores
            venta = {
                "id": int(fila["id"]),
                "fecha": datetime.strptime(fila["sales_date"], "%Y-%m-%d"),
                "monto": float(fila["sales_amount"])
            }
            ventas.append(venta)  # agrego a la lista ventas
    return ventas

# ---------------------------------------------------------
# Ventas totales del año
# ---------------------------------------------------------
def ventas_totales(ventas):
    return sum(v["monto"] for v in ventas)

# ---------------------------------------------------------
# Día con mayor venta
# ---------------------------------------------------------
def dia_mayor_venta(ventas):
    return max(ventas, key=lambda v: v["monto"])

# ---------------------------------------------------------
# Ventas por mes (YYYY-MM)
# ---------------------------------------------------------
def ventas_por_mes(ventas):
    resumen = {}
    for v in ventas:
        mes = v["fecha"].strftime("%Y-%m")
        resumen[mes] = resumen.get(mes, 0) + v["monto"]
    return resumen

# ---------------------------------------------------------
# Mostrar ventas mensuales en forma de tabla
# ---------------------------------------------------------
def mostrar_tabla_ventas_mensuales(ventas_mensuales):
    print("\n=== Ventas por mes ===")
    print(f"{'Mes':<10} | {'Ventas ($)':>12}")
    print("-" * 25)
    for mes, monto in ventas_mensuales.items():
        print(f"{mes:<10} | ${monto:>12,.2f}")

# ---------------------------------------------------------
# Programa principal
# ---------------------------------------------------------
def main():
    ventas = cargar_ventas()

    print("=== Indicadores de Ventas 2024 ===")
    print(f"Ventas totales del año: ${ventas_totales(ventas):,.2f}")

    mayor = dia_mayor_venta(ventas)
    print(f"Día con mayor venta: {mayor['fecha'].strftime('%Y-%m-%d')} (${mayor['monto']:,.2f})")

    ventas_mensuales = ventas_por_mes(ventas)
    mostrar_tabla_ventas_mensuales(ventas_mensuales)

# Ejecutamos
main()
