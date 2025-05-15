#Registro de consumo eléctrico por edificio en la UAM
aulas= biblioteca = administracion = laboratorios = cafeteria = consumo_total= 0

while True:
   print("""******CONSUMO ELECTRICO*******
      1. Ingresar Consumo
      2. Consumo Por Edificio
      3. Consumo Total
      4. Salir """)
   
   opc= int(input("Introduzca la opción: "))

   if opc == 1:
      for i in range(7):
         aulas += float(input("Introduzca el consumo del aula en la mañana"))
         aulas += float(input("Introduzca el consumo del aula en la tarde"))
         aulas += float(input("Introduzca el consumo del aula en la noche"))
         biblioteca += float(input("Introduzca el consumo de la biblioteca en la mañana"))
         biblioteca += float(input("Introduzca el consumo de la biblioteca en la tarde"))
         biblioteca += float(input("Introduzca el consumo de la biblioteca en la noche"))
         administracion += float(input("Introduzca el consumo de la administración en la mañana"))
         administracion += float(input("Introduzca el consumo de la administracion en la tarde"))
         administracion += float(input("Introduzca el consumo de la administracion en la noche"))
         laboratorios += float(input("Introduzca el consumo de la administración en la laboratorios "))
         laboratorios += float(input("Introduzca el consumo de la administracion en la laboratorios"))
         laboratorios += float(input("Introduzca el consumo de la administracion en la laboratorios"))
         cafeteria += float(input("Introduzca el consumo de la cafeteria en la mañana"))
         cafeteria += float(input("Introduzca el consumo de la cafeteria en la tarde"))
         cafeteria += float(input("Introduzca el consumo de la cafeteria en la noche"))
   elif opc == 2:
      print(f"""El consumo de aulas fue de: {aulas}
            El consumo de biblioteca fue de: {biblioteca}
            El consumo de administracion fue de: {administracion}
            El consumo de laboratorios fue de: {laboratorios}
            El consumo de cafeteria fue de: {cafeteria}""")
      
   elif opc == 3:
      consumo_total= aulas + biblioteca + administracion + laboratorios + cafeteria
      print(f"El consumo total de energia electrica de la semana fue de: {consumo_total}")
   else:
      print("Ha salido del programa")
      break