# Programa para llevar registro de ventas en feria UAM
# Autor: [Tu nombre]
# Fecha: [Fecha actual]

def main():
    print("Sistema de control de ventas - Feria UAM")
    print("=======================================\n")
    
    # Definición de estructura de datos
    dias = ["Día 1", "Día 2", "Día 3"]
    stands_por_dia = 4
    productos_por_stand = 3
    
    # Matriz tridimensional para almacenar ventas: [día][stand][producto]
    ventas = [[[0 for _ in range(productos_por_stand)] 
              for _ in range(stands_por_dia)] 
             for _ in range(len(dias))]
    
    # Totales
    total_por_dia = [0] * len(dias)
    total_por_stand = [[0 for _ in range(stands_por_dia)] for _ in range(len(dias))]
    total_general = 0
    
    # Encabezado
    print("Ingrese las ventas para cada producto:\n")
    
    # Recorrer días
    for i in range(len(dias)):
        print(f"\n╔═════════════════════════════════════════╗")
        print(f"║              {dias[i]}                  ║")
        print(f"╚═════════════════════════════════════════╝")
        
        # Recorrer stands
        for j in range(stands_por_dia):
            print(f"\nStand {j+1}:")
            
            # Recorrer productos
            for k in range(productos_por_stand):
                while True:
                    try:
                        monto = float(input(f"Ingrese ventas del producto {k+1}: C$"))
                        if monto < 0:
                            print("Error: Ingrese un valor positivo.")
                            continue
                        ventas[i][j][k] = monto
                        total_por_dia[i] += monto
                        total_por_stand[i][j] += monto
                        total_general += monto
                        break
                    except ValueError:
                        print("Error: Ingrese un valor numérico válido.")
    
    # Mostrar resultados
    print("\n\n╔═════════════════════════════════════════╗")
    print("║          RESUMEN DE VENTAS            ║")
    print("╚═════════════════════════════════════════╝")
    
    # Por día
    print("\nVentas por día:")
    for i in range(len(dias)):
        print(f"{dias[i]}: C${total_por_dia[i]:.2f}")
    
    # Por stand
    print("\nVentas por stand:")
    for i in range(len(dias)):
        print(f"\n{dias[i]}:")
        for j in range(stands_por_dia):
            print(f"  Stand {j+1}: C${total_por_stand[i][j]:.2f}")
    
    # Total general
    print(f"\nTOTAL GENERAL DE LA FERIA: C${total_general:.2f}")

if __name__ == "_main_":
    main()