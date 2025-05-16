"""Implemente un programa que simule el estado de uso de computadoras en dos laboratorios del
campus. Cada laboratorio contiene cinco filas de cuatro computadoras. Por cada computadora se
debe registrar si está ocupada o libre (puede ingresarse manualmente o simularse con valores
aleatorios). Al finalizar, el programa debe mostrar el resumen de computadoras ocupadas y libres
por laboratorio."""

import random #para valores aleatorios

laboratorios = ["Laboratorio 1", "Laboratorio 2"]
computadorasLab1 = [
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0]
]
computadorasLab2 = [
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0]
]
#Aqui se decide si los datos se generaran automaticamente
modoInputDatos = input("Desea generar los datos aleatoriamente?(Y/N): ").strip().upper()
for lab in range(2):
            print(f"""\n
╔═════════════════════════════════════╗
            {laboratorios[lab]}
╚═════════════════════════════════════╝""")
            if lab == 0:
                    computadoras = computadorasLab1
            else:
                    computadoras = computadorasLab2
            for filas in range(5):
                    for columnas in range(4):
                        if modoInputDatos == "N":
                            while True:
                                estado = input("Computadora de la fila " + str(filas + 1) + ", columna " + str(columnas + 1) + " libre (L) u ocupada (O): ").strip().upper()
                                if estado == "L":
                                    computadoras[filas][columnas] = 0
                                    break
                                elif estado == "O":
                                    computadoras[filas][columnas] = 1
                                    break
                                else:
                                    print("Error: Debe ingresar L(Libre) u (Ocupado)O.\n")
                        else:       
                            computadoras[filas][columnas] = random.randint(0, 1)  #Aqui se generan los datos aleatorios (0 = libre, 1 = ocupada)
                                
for lab in range(2):
    print(f"""\n
╔═════════════════════════════════════╗
     Estados de {laboratorios[lab]}
╚═════════════════════════════════════╝""")
    
    if lab == 0:
        computadoras = computadorasLab1
    else:
        computadoras = computadorasLab2

    ocupadas = 0
    libres = 0

    for i in range(5):
        linea = "Fila " + str(i + 1) + ": "
        for j in range(4):
            if computadoras[i][j] == 1:
                linea += "O "
                ocupadas += 1
            else:
                linea += "L "
                libres += 1
        print(linea)

    #Mostramos el resumen de computadoras ocupadas y libres de cada lab
    print("╔═════════════════════════════════════╗")
    print(" Resumen de", laboratorios[lab] + ":")
    print(" Computadoras ocupadas:", ocupadas)
    print(" Computadoras libres:", libres)
    print("╚═════════════════════════════════════╝")
                            
