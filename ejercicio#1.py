"""Caso 1: Control de venta de vigorón en feria universitaria UAM
Desarrolle un programa que permita simular la venta de vigorón durante una feria gastronómica
organizada en la Universidad Americana, UAM Managua. El sistema debe solicitar la cantidad
de clientes atendidos y, por cada cliente, cuántas porciones de vigorón compró, junto con el
precio unitario por porción. El programa debe calcular el total pagado por cada cliente y mostrar
el total de ventas de toda la feria. Utilice estructuras cíclicas anidadas."""

# Programa de venta de vigorón en la UAM


def main():
    print("Sistema de control de ventas de vigorón - Feria UAM")
    print("===================================================\n")
    
    # Solicitar cantidad de clientes (con validación)
    num_clientes = 0
    while num_clientes <= 0:
        try:
            num_clientes = int(input("Ingrese la cantidad de clientes atendidos: "))
            if num_clientes <= 0:
                print("Error: Ingrese un número mayor que cero.")
        except ValueError:
            print("Error: Debe ingresar un número entero.")
            num_clientes = 0  # Reiniciar para repetir el ciclo
    
    total_feria = 0  # Acumulador del total de ventas
    
    # Procesar cada clientekdfhdhfshdhfhdsd
    for i in range(1, num_clientes + 1):
        print(f"\nCliente #{i}")
        
        # Validar la cantidad de las porciones
        porciones = 0
        while porciones <= 0:
            try:
                porciones = int(input("Ingrese la cantidad de porciones compradas: "))
                if porciones <= 0:
                    print("Error: Ingrese un número mayor que cero.")
            except ValueError:
                print("Error: Debe ingresar un número entero.")
                porciones = 0  # Reiniciar para repetir
        
        # Validar precio por cada porción
        precio = 0.0
        while precio <= 0:
            try:
                precio = float(input("Ingrese el precio por porción (C$): "))
                if precio <= 0:
                    print("Error: Ingrese un valor mayor que cero.")
            except ValueError:
                print("Error: Debe ingresar un número válido.")
                precio = 0.0  # Reiniciar para repetir
        
        # Calcular total del cliente
        total_cliente = porciones * precio
        print(f"Total a pagar: C${total_cliente:.2f}")
        
        # Sumar al total de la feria
        total_feria += total_cliente
    
    # Mostrar resumen final
    print("\nResumen de ventas")
    print("=================")
    print(f"Clientes atendidos: {num_clientes}")
    print(f"Total vendido en la feria: C${total_feria:.2f}")

if __name__ == "_main_":
    main()