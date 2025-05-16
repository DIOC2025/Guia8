"""Caso 3: Cálculo de promedio académico en la UAM

Elabore un programa que procese las calificaciones de varios estudiantes de la carrera de
Ingeniería en Sistemas de la Información en la UAM. Por cada estudiante, se ingresarán las
calificaciones de tres asignaturas, y cada asignatura incluirá tres tareas y un examen. El
programa debe calcular el promedio por asignatura y el promedio general del estudiante. Utilice
estructuras cíclicas anidadas para manejar estudiantes, asignaturas y evaluaciones."""""

print ("Calculo de promedio calificacion de UAM")


Nasig = 0
Nestu = 0


print("Cálculo de promedio calificación de UAM")
print("Cuando desee finalizar el proceso ingrese 0 en las dos primeras tareas de una asignatura (sig1=0 y sig2=0)")

Nestu = 0
# bandera para detener ambos bucles cuando el usuario quiera salir
terminar = False

while not terminar:
    Nestu += 1
    print("\n=== Estudiante", Nestu, "===\n")
    
    suma_prom_asigs = 0.0  # acumula promedios de cada asignatura
    
    # recorremos 3 asignaturas por estudiante
    for Nasig in range (1,4):
        print (f"---Asignatura{Nasig}---")
         
        sig1 = float(input("Ingrese la nota de la tarea 1: "))
        sig2 = float(input("Ingrese la nota de la tarea 2: "))
        
        if sig1 == 0 and sig2 == 0:
         terminar = True
         break

        sig3 = float(input("Ingrese la nota de la tarea 3: "))
        exam1 = float(input("Ingrese la nota del examen: "))
        
        # promedio de la asignatura
        prom = (sig1 + sig2 + sig3 + exam1) / 3
        print(f"Promedio Asignatura {Nasig}: {prom:.2f}\n")
        
        suma_prom_asigs += prom
    
    if terminar:
        print("\nProceso finalizado por el usuario.")
        break
    
    # promedio general del estudiante
    prom_general = suma_prom_asigs 
    print(f">>> Promedio general Estudiante {Nestu}: {prom_general:.2f}\n")

print("Fin del programa.")