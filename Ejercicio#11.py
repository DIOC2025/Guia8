"""Registro de asistencia académica
Desarrolle un programa que registre la asistencia de estudiantes en tres secciones distintas de la
UAM, durante cinco días de clases. Cada día se tomará asistencia a seis estudiantes por sección.
El programa deberá contabilizar y mostrar el total de asistencias registradas por sección, así como
el total general de la semana"""

#Definimos los valores ya conocidos
diasSemana = ["Lunes", "Martes", "Miercoles"," Jueves", "Viernes"]
secciones = ["Seccion 1", "Seccion 2", "Seccion 3"]
estudiantesSeccion = 6
asistencia = [
    [0, 0, 0], #Lunes
    [0, 0, 0], #Martes
    [0, 0, 0], #Miercoles
    [0, 0, 0], #Jueves
    [0, 0, 0] #Viernes
]
total = [0,0,0]
#Recorremos secciones
for seccion in range (3):
        print(f"""\n
╔═════════════════════════════════════╗
              {secciones[seccion]}
╚═════════════════════════════════════╝""")
        #Recorremos dias de la semana
        for dia in range(5):
                       print(f"""\n
╔═════════════════════════════════════════╗
              Dia: {diasSemana[dia]}              
╚═════════════════════════════════════════╝""") 
                       #Recorremos estudiantes
                       for estudiante in range(estudiantesSeccion):
                               print("""
╔═════════════════════════════════════════╗
║Recordatorio: Presente (P), Ausente (A)  ║ 
╚═════════════════════════════════════════╝""")
                               while True:
                                        
                                        print("CONFIRMAR ASISTENCIA DEL ESTUDIANTE")
                                        presente = input(f"Estudiante #{estudiante+1}(P/A): ").capitalize().strip()
                                        if presente in ['P', 'A']:
                                                if presente == 'P':
                                                        asistencia[dia][seccion] += 1
                                                        total [seccion] +=1
                                                break
                                        else:
                                                print("\n Error: Ingrese P(Presente) o A(Ausente)")
print("""
╔═════════════════════════════════════════╗
║           Datos de asistencia           ║ 
╚═════════════════════════════════════════╝
      """)              

for i in range(3):
        print(f"\t -Total de asistencias en la {secciones[i]}: {total[i]}")

print(f"""
╔═════════════════════════════════════════╗
║  Total de asistencias: {sum(total)}              ║ 
╚═════════════════════════════════════════╝
      """)

                                

