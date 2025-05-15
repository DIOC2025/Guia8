"""Caso 9: Evaluación del acceso a internet en hogares de estudiantes
Implemente un programa que simule una encuesta realizada a estudiantes de la UAM para
conocer su acceso a internet en casa. Se trabajará con tres carreras, cada una con tres grupos,
y se entrevistará a cinco estudiantes por grupo. Se debe registrar si el estudiante tiene acceso
estable, intermitente o no tiene internet. Al final, mostrar un conteo de cada tipo de acceso por
carrera y el total general.
"""

print("Encuesta: Acceso a internet en casa.")

#Primero se definen datos que ya conocemos
carreras = ["Medicina", "Ingenieria en Sistemas", "Aquitectura"]
gruposCarrera = 3
estudiantesGrupo = 5
tiposInternet = ["Estable", "Intermitente", "Nulo"]
#Aqui se hace un arreglo bidimensional para almacenar las respuestas por cada carrera
resultados = [
    #Medicina
    [0, 0, 0],
    #Ingenieria en sistemas
    [0, 0, 0],
    #Arquitectura
    [0, 0, 0]
]
#Aqui se hace otro arreglo bidimensional que guarde los datos totales
total = [0, 0, 0]

#Recorremos las carreras y grupos, empezamos el formulario
for i in range (3):
    print(f"Carrera: {carreras[i]}")
    #Recorremos grupos
    for g in range(3):
        #Recorremos personas
        for h in range (5):
            #Añadimos un while para confirmar que se ingresen los datos necesarios para que el programa funcione como es debido
            while True:
                print(f"Tipos de acceso: {tiposInternet}")
                #Capitalize y strip se utilizan para añadir mayuscula inicial a palabras y para eliminar espacios que puedan afectar 
                #el reconocimiento de la palabra ingresada
                tipoAcceso = input("Ingrese su tipo de acceso a internet").capitalize().strip
                if tipoAcceso  in tiposInternet:
                    indice = tipoAcceso(tiposInternet)
                    resultados[i][indice] +=1
                    total [indice] +=1
                else:
                    print("Error: Ingrese uno de los tipos de acceso que se muestran arriba.")

                    KIERO SMEMEN!!!!