def funcion_imprimir(p_trabajadores, p_cargo_imprmir):
    with open ("planilla.txt", "w", newline="") as archivo :
        for i in range(len(p_trabajadores)):
            desc_salud = p_trabajadores[i]["sueldo_bruto"] * 7/100
            desc_afp = p_trabajadores[i]["sueldo_bruto"] * 12/100
            sueld_luiq = p_trabajadores[i]["sueldo_bruto"] - desc_afp - desc_salud

            if p_trabajadores[i]["cargo"] == p_cargo_imprmir:
                escritor = archivo.write("Trabajador | Cargo | Sueldo Bruto | Desc. Salud | Desc. AFP | Luiquido a pagar \n")
                escritor = archivo.write(f"{p_trabajadores[i]["nombre"]} | {p_trabajadores[i]["cargo"]} | {p_trabajadores[i]["sueldo_bruto"]} | {desc_salud} | {desc_afp}")

def funcion_imprimir_trabajadores(p_trabajadores):
    for i in range(len(p_trabajadores)):
        des_salud = p_trabajadores[i]["sueldo_bruto"] * 7/100
        des_afp = p_trabajadores[i]["sueldo_bruto"] * 12/100
        sueldo_liquido = p_trabajadores[i]["sueldo_bruto"] - des_afp - des_salud
        print(f"Trabajadores: {p_trabajadores[i]["nombre"]} | Cargo {p_trabajadores[i]["cargo"]} | Sueldo Bruto: {p_trabajadores[i]["sueldo_bruto"]} | Descuento Salud: {des_salud} | Desc. AFP: {des_afp} | Liquido a pagar: {sueldo_liquido} ")

def pedir_datos(p_trabajadores):
    trabajador = input("Ingrese el nombre del trabajador: ")
    cargo = input("Ingrese el cargo del trabajador: ")
    sueldo_burto = int(input("Ingrese el sueldo burto del trabajador: "))

    trabajador = {
        "nombre": trabajador,
        "cargo": cargo,
        "sueldo_bruto": sueldo_burto
    }

    p_trabajadores.append(trabajador)