"""
GeorgeTown Cleaning Servives es una pequeña lavanderia. Procesa camisas, pantalones y vestidos. Desea que usted diseñe el
sistema de facturacion. Debe tener en consideracion los siguientes puntos:

Cada camisa cuesta $0.75
Cada pandatalon cuesta $2.25
Cada vestido cuesta $4.75

La tasa de impuesto es de un 18%
Se desea imprimir un recibo detallado para cada cliente
No hay descuento
"""

import datetime 


camisa = 0.75
pantalon = 2.25
vestido = 4.75

print("\n -/- GeorgeTown Cleaning Services -/- \n")

#Pedir los datos del cliente

nombre = str(input("Ingrese su nombre: "))
telefono = str(input("Ingrese su telefono: "))

fecha = datetime.datetime.now()

fecha = fecha.strftime("%Y-%m-%d %H:%M:%S")

cantidad_camisas = int(input("Ingrese la cantidad de camisas: "))
cantidad_pantalones = int(input("Ingrese la cantidad de pantalones: "))
cantidad_vestidos = int(input("Ingrese la cantidad de vestidos: "))

subtotal_camisas = cantidad_camisas * camisa
subtotal_pantalones = cantidad_pantalones * pantalon
subtotal_vestidos = cantidad_vestidos * vestido


subtotal = subtotal_camisas + subtotal_pantalones + subtotal_vestidos
total = subtotal * 18 / 100
total_del_total = subtotal + total

print(f"El total de su compra es ${subtotal:.2f}, mas el ITBIS ${total:.2f}, el total es = ${total_del_total:.2f}")

pago = float(input("Digite su pago: "))

valor_total =  pago - total_del_total

print("""
      ====================================
      -/- GeorgeTown Cleaning Services -/-
      ====================================
      """)
print(f"      Customer Name: {nombre}")
print(f"      Customer Tel: {telefono}")
print(f"      Order date: {fecha}")
print(f"""
      --------------------------------------
      Item      Qty     Unit/Price  Subtotal
      --------------------------------------
      Shirt     {cantidad_camisas:>2}  {camisa:>10} {subtotal_camisas:>10} 
      Pants     {cantidad_pantalones:>2} {pantalon:>10}{subtotal_pantalones:>10}
      Dresses   {cantidad_vestidos:>2}{vestido:>10}{subtotal_vestidos:>10}
      --------------------------------------
      Sub-total:    {subtotal:.2f}
      Tax Rate:     18%
      Taxe:         {total:.2f}
      Net Sales:    {total_del_total:.2f}
      Paymen Due:   {pago:.2f}
      Change:       {valor_total:.2f}
      --------------------------------------
      Gracias por su compra.
      """)

