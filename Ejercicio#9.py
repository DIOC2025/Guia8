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
    print(f"""\n
╔═════════════════════════════════════════╗
        Carrera: {carreras[i]}
╚═════════════════════════════════════════╝""")
    #Recorremos grupos
    for g in range(3):
        print(f"""\n
╔═════════════════════════════════════════╗
              Grupo: {g+1}
╚═════════════════════════════════════════╝""")
        #Recorremos personas
        for h in range (5):
            #Añadimos un while para confirmar que se ingresen los datos necesarios para que el programa funcione como es debido
            while True:
               #Un for para mostrar los tipos enumerados para que el usuario solo tenga que ingresar el num
               for indice, tipoInt in enumerate(tiposInternet):
                   print(f"{indice+1}. {tipoInt}")
               opc = (input("Ingrese el tipo de acceso de internet que posee(1 - 3): ")).strip()
               if opc.isdigit():
                    #convertimos el input a entero ya que no podriamos usar .strip()
                    opcNum = int(opc)
                    if 1 <= opcNum <=3:
                        index  = opcNum -1
                        resultados[i][index]+=1
                        total[index]+=1
                        break
                    else:
                        print("Ingrese un numero dentro del rango (1 - 3)")
               else: 
                    print("Porfavor ingrese un numero(1 - 3)")

print(f"""
╔═════════════════════════════════════════╗
║       Resultados de la encuesta         ║ 
╚═════════════════════════════════════════╝
""")

for i in range(3):
    print(f"""
╔═════════════════════════════════════════╗
║ Carrera: {carreras[i]}                  
╚═════════════════════════════════════════╝""")
    for j in range(3):
        print(f"  - {tiposInternet[j]}: {resultados[i][j]} estudiante(s)")

print(f"""
╔═════════════════════════════════════════╗
║     Resultados totales de la encuesta   ║ 
╚═════════════════════════════════════════╝""")
for k in range(3):
    print(f"  - {tiposInternet[k]}: {total[k]} estudiante(s)")