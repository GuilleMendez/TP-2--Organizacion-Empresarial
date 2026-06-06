# Montamos Google Drive para acceder a los archivos del usuario
from google.colab import drive
drive.mount('/content/drive')

# Cambiamos el directorio de trabajo al lugar donde está el CSV
%cd /content/drive/MyDrive/Colab Notebooks/TP Intengrador/AnalisisDeVentas

import csv
from datetime import datetime

# ---------------------------------------------------------
# Cargar ventas desde el archivo CSV
# ---------------------------------------------------------
def cargar_ventas():
    ventas = []  # Lista donde vamos a guardar cada venta como un diccionario

    # Abrimos el archivo CSV en modo lectura
    with open("/content/drive/MyDrive/Colab Notebooks/TP Intengrador/AnalisisDeVentas/sales_sample_2024.csv",
              "r", encoding="utf-8") as archivo:

        lector = csv.DictReader(archivo)  # Lee el CSV como diccionarios

        # Recorremos cada fila del archivo
        for fila in lector:
            venta = {
                "id": int(fila["id"]),  # Convertimos el ID a entero
                "fecha": datetime.strptime(fila["sales_date"], "%Y-%m-%d"),  # Convertimos la fecha a objeto datetime
                "monto": float(fila["sales_amount"])  # Convertimos el monto a número decimal
            }
            ventas.append(venta)  # Agregamos la venta a la lista

    return ventas  # Devolvemos la lista completa de ventas


# ---------------------------------------------------------
# Ventas totales del año
# ---------------------------------------------------------
def ventas_totales(ventas):
    # Sumamos el campo "monto" de cada venta usando una expresión generadora
    return sum(v["monto"] for v in ventas)


# ---------------------------------------------------------
# Día con mayor venta
# ---------------------------------------------------------
def dia_mayor_venta(ventas):
    # Usamos max() con una función lambda para encontrar la venta con mayor monto
    return max(ventas, key=lambda v: v["monto"])


# ---------------------------------------------------------
# Ventas por mes (YYYY-MM)
# ---------------------------------------------------------
def ventas_por_mes(ventas):
    resumen = {}  # Diccionario donde acumularemos las ventas por mes

    for v in ventas:
        mes = v["fecha"].strftime("%Y-%m")  # Convertimos la fecha al formato "Año-Mes"

        # Si el mes no existe en el diccionario, lo crea con valor 0
        # Luego suma el monto de la venta
        resumen[mes] = resumen.get(mes, 0) + v["monto"]

    return resumen  # Devolvemos el resumen mensual


# ---------------------------------------------------------
# Mostrar ventas mensuales en forma de tabla
# ---------------------------------------------------------
def mostrar_tabla_ventas_mensuales(ventas_mensuales):
    print("\n=== Ventas por mes ===")
    print(f"{'Mes':<10} | {'Ventas ($)':>12}")  # Encabezado de la tabla
    print("-" * 25)

    # Recorremos el diccionario e imprimimos cada mes con su total
    for mes, monto in ventas_mensuales.items():
        print(f"{mes:<10} | ${monto:>12,.2f}")  # Formato con comas y 2 decimales


# ---------------------------------------------------------
# Programa principal
# ---------------------------------------------------------
def main():
    ventas = cargar_ventas()  # Cargamos todas las ventas desde el CSV

    print("=== Indicadores de Ventas 2024 ===")
    print(f"Ventas totales del año: ${ventas_totales(ventas):,.2f}")  # Mostramos total anual

    mayor = dia_mayor_venta(ventas)  # Obtenemos la venta más alta
    print(f"Día con mayor venta: {mayor['fecha'].strftime('%Y-%m-%d')} (${mayor['monto']:,.2f})")

    ventas_mensuales = ventas_por_mes(ventas)  # Calculamos ventas por mes
    mostrar_tabla_ventas_mensuales(ventas_mensuales)  # Mostramos la tabla


# Ejecutamos el programa principal
main()


