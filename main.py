import os
from functions import *

os.system("cls")

trabajadores = []
cargos = []
sueldos_burto = []

while True:
    print("Menú")
    print("-"*50)
    print("1. Registrar trabajador")
    print("2. Listar todos los trabajadores")
    print("3. Imprimir planilla de sueldos")
    print("4. Salir del programa")
    print("-"*50)
    opc = int(input("Ingrese la opción que deseea: "))

    os.system("cls")

    if opc == 1:
        pedir_datos(trabajadores)
    elif opc == 2:
        funcion_imprimir_trabajadores(trabajadores)
    elif opc == 3:
        cargo_imprimir = input("Ingrese el cargo que deseea imprimir: ")
        funcion_imprimir(trabajadores, cargo_imprimir)
    else:
        print("Adiós!")
        break