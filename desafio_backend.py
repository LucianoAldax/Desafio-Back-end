from os import system
import sqlite3
import datetime
import sys

######### CREAR DB SI NO EXISTE #########


def crearDB():
    conn = sqlite3.connect('IMPUESTOS.db')
    c = conn.cursor()

    c.execute(""" CREATE TABLE IF NOT EXISTS tablaBoletas (
        CODIGO TEXT PRIMARY KEY NOT NULL,
        tipo TEXT,
        descripcion TEXT,
        fecha_venc TEXT,
        importe REAL,
        estado TEXT,
        metodo_pago TEXT,
        num_tarj TEXT,
        fecha_pago TEXT) """)

    conn.commit()

    conn.close

######### MENU PRINCIPAL ###########


def menu():
    system("cls")
    opc = int(input("Menú principal \n" +
                    "1. Crear Boleta \n" +
                    "2. Pagar Boleta \n" +
                    "3. Ver Boletas \n" +
                    "4. Filtrar Boletas por fecha \n" +
                    "0. Salir \n" +
                    "\nElija una opción: "))

    return opc


################# CREACION DE BOLETA #################

def crearTipo():

    opc = int(input("Crear Boleta \n" +
                    "1. Boleta de Luz \n" +
                    "2. Boleta de Gas \n" +
                    "3. Boleta de Agua \n" +
                    "0. Volver \n" +
                    "\nElija una opción: "))

    if opc == 1:
        tipo = "Luz"
    elif opc == 2:
        tipo = "Gas"
    elif opc == 3:
        tipo = "Agua"
    elif opc == 0:
        system("cls")
        menu()
    return tipo


def crearDescrip():
    descrp = input("Crear Boleta \n" +
                   "Descripcion \n" +
                   "\nIngrese una descripción: ")

    return descrp


def crearVencimiento():
    fvenc = input("Crear Boleta \n" +
                  "Fecha de Vencimiento \n" +
                  "\nIngrese una fecha de vencimiento en formato YYYY-MM-DD: ")

    return fvenc


def crearImporte():
    importe = input("Crear Boleta \n" +
                    "Importe \n" +
                    "\nIngrese un importe: ")

    return importe


def crearEstado():

    opc = int(input("Crear Boleta \n" +
                    "Seleccione el estado \n" +
                    "1. Pendiente \n" +
                    "2. Pagado \n" +
                    "\nElija una opción: "))

    if opc == 1:
        estado = "Pendiente"
    elif opc == 2:
        estado = "Pagado"

    return estado


def crearCodigo():
    codigob = input("Crear Boleta \n" +
                    "Código de Barra \n" +
                    "\nIngrese el código de barra: ")
    return codigob


def guardarBoleta(tipo, descp, fvenc, importe, estado, codigob):

    conn = sqlite3.connect('IMPUESTOS.db')
    c = conn.cursor()

    c.execute("INSERT INTO tablaBoletas (tipo, descripcion, fecha_venc, importe, estado, CODIGO) VALUES (?, ?, ?, ?, ?, ?)",
              (tipo, descp, fvenc, importe, estado, codigob))

    conn.commit()
    conn.close()


################ PAGO DE BOLETA ################

def pagarTipo():

    opc = int(input("Pagar Boleta \n" +
                    "1. Tarjeta de Débito \n" +
                    "2. Tarjeta de Crédito \n" +
                    "3. Efectivo \n" +
                    "0. Volver \n" +
                    "\nElija una opción: "))

    if opc == 1:
        tipo = "debito"
    elif opc == 2:
        tipo = "credito"
    elif opc == 3:
        tipo = "efectivo"
    elif opc == 0:
        system("cls")
        menu()
    return tipo


def numTarjeta():
    numT = input("Pagar Boleta \n" +
                 "Número de tarjeta \n" +
                 "\nIngrese el número de la tarjeta: ")
    return numT


def pagarImporte():
    importe = input("Pagar Boleta \n" +
                    "Importe \n" +
                    "\nIngrese un importe: ")

    return importe


def pagoCodigo():
    codigob = input("Pagar Boleta \n" +
                    "Código de Barra \n" +
                    "\nIngrese el código de barra: ")
    return codigob


def pagarBoleta(tipo, num, codigob):

    fecha = datetime.datetime.now()
    fpago = fecha.strftime("%Y-%m-%d")

    conn = sqlite3.connect('IMPUESTOS.db')
    c = conn.cursor()
    estado = "Pagado"
    c.execute("UPDATE tablaBoletas set metodo_pago= ?, num_tarj= ?, estado= ?, fecha_pago= ? where CODIGO == ?",
              (tipo, num, estado, fpago, codigob))

    conn.commit()
    conn.close()


################## VER BOLETAS #######################

def verBoletas():

    opc = int(input("Ver Boletas \n" +
                    "1. Todas \n" +
                    "2. Pagas \n" +
                    "3. Impagas \n" +
                    "0. Volver \n" +
                    "\nElija una opción: "))

    if opc == 1:
        filtro1 = "Todas"
    elif opc == 2:
        filtro1 = "Pagado"
    elif opc == 3:
        filtro1 = "Pendiente"
    elif opc == 0:
        system("cls")
        menu()
    return filtro1


def verBoletasFiltro():

    opc = int(input("Ver Boletas \n" +
                    "1. Todas \n" +
                    "2. Luz \n" +
                    "3. Gas \n" +
                    "4. Agua \n" +
                    "0. Volver \n" +
                    "\nElija una opción: "))

    if opc == 1:
        filtro2 = "Todas"
    elif opc == 2:
        filtro2 = "Luz"
    elif opc == 3:
        filtro2 = "Gas"
    elif opc == 4:
        filtro2 = "Agua"
    elif opc == 0:
        system("cls")
        menu()
    return filtro2


def mostrarTodasBoletas():
    conn = sqlite3.connect('IMPUESTOS.db')
    c = conn.cursor()
    c.execute("SELECT tablaBoletas.tipo, tablaBoletas.fecha_venc, tablaBoletas.importe, tablaBoletas.CODIGO  FROM tablaBoletas")
    for row in c.fetchall():
        print("\n", row[0], "   ", row[1], "    ", row[2], "    ", row[3])
    c.close()


def mostrarFiltroBoletas1(filtro1):
    conn = sqlite3.connect('IMPUESTOS.db')
    c = conn.cursor()
    c.execute("SELECT tablaBoletas.tipo, tablaBoletas.fecha_venc, tablaBoletas.importe, tablaBoletas.CODIGO FROM tablaBoletas where estado == ?", (filtro1,))
    for row in c.fetchall():
        print("\n", row[0], "   ", row[1], "    ", row[2], "    ", row[3])
    c.close()


def mostrarFiltroBoletas2(filtro2):
    conn = sqlite3.connect('IMPUESTOS.db')
    c = conn.cursor()
    c.execute("SELECT tablaBoletas.fecha_venc, tablaBoletas.importe, tablaBoletas.CODIGO  FROM tablaBoletas where tipo == ?", (filtro2,))
    for row in c.fetchall():
        print("\n", row[0], "   ", row[1], "    ", row[2])
    c.close()


def mostrarFiltroBoletas3(filtro2, filtro1):
    conn = sqlite3.connect('IMPUESTOS.db')
    c = conn.cursor()
    c.execute("SELECT tablaBoletas.fecha_venc, tablaBoletas.importe, tablaBoletas.CODIGO  FROM tablaBoletas where tipo == ? and estado == ?", (filtro2, filtro1))
    for row in c.fetchall():
        print("\n", row[0], "   ", row[1], "    ", row[2])
    c.close()

################### FILTRAR POR FECHA ###################


def ingresoPrimeraFecha():
    fecha1 = input("Filtrar Boletas por Fecha \n" +
                   "Fecha de inicio \n" +
                   "\nIngrese una fecha en formato YYYY-MM-DD: ")

    return fecha1


def ingresoSegundaFecha():
    fecha2 = input("Filtrar Boletas por Fecha \n" +
                   "Fecha límite \n" +
                   "\nIngrese una fecha en formato YYYY-MM-DD: ")

    return fecha2


def mostrarFiltroBoletasDiario(fecha1, fecha2):
    conn = sqlite3.connect('IMPUESTOS.db')
    c = conn.cursor()
    c.execute("SELECT tablaBoletas.fecha_pago, tablaBoletas.importe, tablaBoletas.CODIGO  FROM tablaBoletas where estado == 'Pagado' and tablaBoletas.fecha_pago BETWEEN ? and ?", (fecha1, fecha2))
    res = 0
    for row in c.fetchall():
        print("\n", row[0], "   ", row[1], "    ", row[2])
        res = float(row[1]) + res

    print("\n\n\nCantidad de Transacciones: ", len(row) - 1)
    print("\nImporte acumulado: $", res)
    c.close()


#################### FUNCION MAIN #######################
if __name__ == '__main__':
    crearDB()

    opt = 1

    while opt > 0:
        opt = menu()

        if opt == 1:
            system("cls")
            tipo = crearTipo()
            system("cls")
            descp = crearDescrip()
            system("cls")
            fvenc = crearVencimiento()
            system("cls")
            importe = crearImporte()
            system("cls")
            estado = crearEstado()
            system("cls")
            codigb = crearCodigo()
            system("cls")
            guardarBoleta(tipo, descp, fvenc, importe, estado, codigb)

        elif opt == 2:
            system("cls")
            tipo = pagarTipo()
            system("cls")
            if tipo != "efectivo":
                numT = numTarjeta()
            else:
                numT = "-"

            system("cls")
            codigob = pagoCodigo()
            system("cls")

            pagarBoleta(tipo, numT, codigob)

        elif opt == 3:
            system("cls")
            filtro1 = verBoletas()
            system("cls")
            filtro2 = verBoletasFiltro()
            if filtro1 == "Todas" and filtro2 == "Todas":

                mostrarTodasBoletas()
                input("Press Enter to continue...")
            elif filtro1 != "Todas" and filtro2 == "Todas":

                mostrarFiltroBoletas1(filtro1)
                input("Press Enter to continue...")
            elif filtro1 == "Todas" and filtro2 != "Todas":

                mostrarFiltroBoletas2(filtro2)
                input("Press Enter to continue...")
            else:

                mostrarFiltroBoletas3(filtro2, filtro1)
                input("Press Enter to continue...")

        elif opt == 4:
            system("cls")
            fecha1 = ingresoPrimeraFecha()
            system("cls")
            fecha2 = ingresoSegundaFecha()
            system("cls")
            mostrarFiltroBoletasDiario(fecha1, fecha2)
            input("\nPress Enter to continue...")

        elif opt == 0:
            system("cls")
            sys.exit()
