##Caso 5: Encuesta sobre transporte estudiantil en la UAM 

# creamos arreglos
facultades = ["FIA", "FCAE", "FMC"]
mediosDeTransporte= ["bus", "moto", "taxi","bicicleta", "caminar", "carro"]

## creamos una matriz 3*6
##esto creara una tabla de 6 columnas y 3 filas
conteos = [[0 for _ in range(len(mediosDeTransporte))] for _ in range(len(facultades))]

#creamos otro arreglo
total_general = [0 for _ in range(len(mediosDeTransporte))]
#iniciamos un bucle dentro del rango del arreglo facultades
for i in range(len(facultades)): 
    print(f"\nFACULTAD DE {facultades[i]}") #imprime las facultades dentro de la lista
    for j in range(2): 
        print(f"  Carrera {j + 1}") #suma
        for k in range(5):
             while True: # mientras sea verdadero corre por lo que detenerlo al final
                 medio = input(f"    Estudiante {k + 1}, medio de transporte ({', '.join(mediosDeTransporte)}): ").lower() #lower hace que no importe las minusculas o mayusculas
                 if medio in mediosDeTransporte: #medio es la entrada del usuario e in comprueba si esta en la lista
                     idx = mediosDeTransporte.index(medio) #index devuelve el elemento de la lista que el usuario igreso
                     conteos[i][idx] += 1 #aumenta el contador en las columnas y filas
                     total_general[idx] += 1   # aumenta el total general 
                     break #cierra el bucle
                 else:
                     print("Medio no valido. Intente de nuevo.")
                     
#impresion
print("\nRESULTADOS POR FACULTAD:")
for i in range(len(facultades)):
    print(f"\nFacultad de {facultades[i]}:")
    for j in range(len(mediosDeTransporte)):
        print(f"  {mediosDeTransporte[j].capitalize()}: {conteos[i][j]}") # capitalize hace que la primera letra sea mayuscula y conteos i j devuelve la variable que se encuentra almacenada en esa casilla

# Mostrar total general
print("\nTOTAL GENERAL:")
for i in range(len(mediosDeTransporte)):
    print(f"  {mediosDeTransporte[i].capitalize()}: {total_general[i]}")
