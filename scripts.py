from google.colab import drive
drive.mount('/content/drive')
%cd /content/drive/MyDrive/Colab Notebooks/TP Intengrador/AnalisisDeVentas

import csv
from datetime import datetime

def cargar_ventas():
    ventas = []
    with open("/content/drive/MyDrive/Colab Notebooks/TP Intengrador/AnalisisDeVentas/sales_sample_2024.csv",
              "r", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            venta = {
                "id": int(fila["id"]),
                "fecha": datetime.strptime(fila["sales_date"], "%Y-%m-%d"),
                "monto": float(fila["sales_amount"])
            }
            ventas.append(venta)
    return ventas

def ventas_totales(ventas):
    return sum(v["monto"] for v in ventas)

def dia_mayor_venta(ventas):
    return max(ventas, key=lambda v: v["monto"])

def ventas_por_mes(ventas):
    resumen = {}
    for v in ventas:
        mes = v["fecha"].strftime("%Y-%m")
        resumen[mes] = resumen.get(mes, 0) + v["monto"]
    return resumen

def mostrar_tabla_ventas_mensuales(ventas_mensuales):
    print("\n=== Ventas por mes ===")
    print(f"{'Mes':<10} | {'Ventas ($)':>12}")
    print("-" * 25)
    for mes, monto in ventas_mensuales.items():
        print(f"{mes:<10} | ${monto:>12,.2f}")

def main():
    ventas = cargar_ventas()
    print("=== Indicadores de Ventas 2024 ===")
    print(f"Ventas totales del año: ${ventas_totales(ventas):,.2f}")

    mayor = dia_mayor_venta(ventas)
    print(f"Día con mayor venta: {mayor['fecha'].strftime('%Y-%m-%d')} (${mayor['monto']:,.2f})")

    ventas_mensuales = ventas_por_mes(ventas)
    mostrar_tabla_ventas_mensuales(ventas_mensuales)

main()
