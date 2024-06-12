import os

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

    if opc == 1:
        trabajador = input("Ingrese el nombre del trabajador: ")
        cargo = input("Ingrese el cargo del trabajador: ")
        sueldo_burto = input("Ingrese el sueldo burto del trabajador: ")

        trabajadores.append(trabajador)
        cargos.append(cargo)
        sueldos_burto.append(sueldo_burto)
    elif opc == 2:
        for i in range(len(trabajadores)):
            print(f"Trabajadores: {trabajadores[i]} | Cargo {cargos[i]} | Sueldo Bruto: {sueldos_burto[i]}")
    elif opc == 3:
        pass
    else:
        print("Adiós!")
        break