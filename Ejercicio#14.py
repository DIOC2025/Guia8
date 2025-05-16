"""Ejercicio 4: Monitoreo del consumo energético
Desarrolle un programa que registre el consumo energético de cuatro edificios del campus
universitario a lo largo de una semana. Por cada día se ingresarán los kilovatios consumidos en tres
turnos: mañana, tarde y noche. El programa debe calcular el consumo total por edificio y generar el
promedio semanal correspondiente."""

def main():
    print("Sistema de monitoreo de consumo energético - UAM")
    print("===============================================")
    
    edificios = ["Edificio A", "Edificio B", "Edificio C", "Edificio D"]
    dias_semana = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]
    turnos = ["Mañana", "Tarde", "Noche"]
    
    consumo = [[[0 for _ in range(len(turnos))] 
              for _ in range(len(dias_semana))] 
             for _ in range(len(edificios))]
    
    total_por_edificio = [0] * len(edificios)
    promedio_semanal = [0] * len(edificios)
    
    print("\nIngrese el consumo en kilovatios (kW) para cada turno:")
    
    for i in range(len(edificios)):
        print(f"\n{edificios[i]}:")
        
        for j in range(len(dias_semana)):
            print(f"\n{dias_semana[j]}:")
            
            for k in range(len(turnos)):
                kw = -1  # Valor inicial inválido para entrar al ciclo
                while kw < 0:
                    try:
                        kw = float(input(f"Consumo en turno de {turnos[k]}: "))
                        if kw < 0:
                            print("Error: El consumo no puede ser negativo")
                    except ValueError:
                        print("Error: Ingrese un valor numerico valido")
                        kw = -1  # Forzar a repetir el ciclo
                
                consumo[i][j][k] = kw
                total_por_edificio[i] += kw
    
    for i in range(len(edificios)):
        promedio_semanal[i] = total_por_edificio[i] / len(dias_semana)
    
    print("\nRESUMEN DE CONSUMO")
    print("=================")
    
    for i in range(len(edificios)):
        print(f"\n{edificios[i]}:")
        print(f"Consumo total: {total_por_edificio[i]:.2f} kW")
        print(f"Promedio diario: {promedio_semanal[i]:.2f} kW")
    
    total_general = sum(total_por_edificio)
    print(f"\nCONSUMO TOTAL DEL CAMPUS: {total_general:.2f} kW")

if __name__ == "_main_":
    main()