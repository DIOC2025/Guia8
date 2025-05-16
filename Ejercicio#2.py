"""Caso 2: Registro semanal de gastos de estudiantes UAM
Cree un programa que simule el control de gastos semanales de un grupo de estudiantes de
primer año de la UAM. El sistema debe procesar datos de 4 semanas, y por cada semana,
ingresar el gasto realizado cada día (7 días por semana). El programa debe calcular el total
gastado por semana y el total acumulado del mes. Utilice bucles anidados para recorrer
semanas y días."""

print (" ")
print("Registro semanal de gastos")
print (" ")

Nsem = 0
Ndias = 0

Ndias = 0
# bandera para detener ambos bucles cuando el usuario quiera salir
terminar = False

while not terminar:
    Nsem += 1
    
    
    suma_gasto_asem = 0.0  # Reinicia el contador de gastoS por semana al final de cada bucle
    
    # Recorremos 7 dias por 4 semanas
    for Nsem in range(1, 5):
        print(f"--- Semana {Nsem} ---")
        
        # ingreso de notas
        Dia1 = float(input("Ingrese el gasto en el dia 1: "))
        Dia2 = float(input("Ingrese el gasto en el dia 2: "))
       
        
        # condición de salida
        if Dia1 == 0 and Dia2 == 0:
            terminar = True
            break
        
        Dia3 = float(input("Ingrese el gasto en el dia 3: "))
        Dia4 = float(input("Ingrese el gasto en el dia 4: "))
        Dia5 = float(input("Ingrese el gasto en el dia 5: "))
        Dia6 = float(input("Ingrese el gasto en el dia 6: "))
        Dia7 = float(input("Ingrese el gasto en el dia 7: "))
        
        # Registro de gastos
        Rgast = Dia1+Dia2+Dia3+Dia4+Dia5+Dia6+Dia7
        print(f"Registro de Gastos {Nsem} semana:  C${Rgast:.2f}\n")
        
        suma_gasto_asem += Rgast
    
    if terminar:
        print("\nProceso finalizado por el usuario.")
        break
    
    # Gasto total en 4 semanas
    Gastotal =  suma_gasto_asem
    print(f">>> Gasto Total en {Nsem} semanas: C${Gastotal:.2f}\n")

print("Fin del programa.")