# Caso 10: Control de préstamos en la biblioteca de la UAM
# Desarrolle un programa que permita registrar los préstamos de libros en la biblioteca de la UAM. 
# Se trabajará con cuatro categorías de libros (ingeniería, salud, derecho y literatura), cada una 
# con tres subcategorías. Por cada subcategoría se registrarán los préstamos de cinco días. El 
# sistema debe mostrar el total de préstamos por subcategoría, categoría y el total general 
# semanal. 
                    
#creamos arreglos.
categoriasLibros = ["ingenieria", "salud", "derecho", "literatura"]
subcategorias = ["subcategoria1","subcategoria2","subcategoria3"]
#creamos una matriz 4*3
conteos = [[0 for _ in range (len(subcategorias))]for _ in range (len(categoriasLibros))]
total = [0 for _ in range(len(categoriasLibros))]
#iniciamos un bucle for con el rengo del arreglo categoriasLibros
for i in range (len(categoriasLibros)):
    print("la categoria es: ", categoriasLibros[i] )
    for j in range (len(subcategorias)):
        print(subcategorias[j])
        prestamos = input("ingrese cuantos prestamos se realizaron dentro de cindo dias: ")
        prestamos = int(prestamos) #convertimos prestamos a numeros enteros
        conteos[i][j] += prestamos 
        total[i] += prestamos  
#imprimimos los datos de las categorias
print("resultados por categorias")
for i in range (len(categoriasLibros)):
    print("categoria de: ", categoriasLibros[i])
    for j in range (len(subcategorias)):
        print(f" {subcategorias[j]. capitalize()} : {conteos[i][j]}")
#imprimimos el total por las categorias
print("total general")
for i in range(len(categoriasLibros)):
    print(f"  {categoriasLibros[i].capitalize()}: {total[i]}")
