#Registra las ventas de Nacatamles los domingos en la uam
acum1= 0
cont1=0
acum2= 0
cont2= 0
acum3= 0
cont3= 0
acum4= 0
cont4= 0

while True:
   print("*************************BIENVENIDOS A LAS VENTAS DE NACATAMALES*******************")
   print("""Elija una opción
      1. Primer Domingo
      2. Segundo Domingo
      3. Tercer Domingo
      4. Cuarto Domingo 
      5. Acumulado Mensual
      6. Salir""")
   opc= int(input("Introduzca su opcion: "))

   if opc == 1:
        print(""""****Venta Primer Domingo*******
          1. Registrar Venta
          2. Salir """)
        opc1= int(input("Introduzca su opcion: "))
        while opc1 == 1:
           nombre= input("Ingrese nombre del cliente: ")
           cont1 += 1
           cantidad= int(input("Ingrese la cantidad de nacatamales que compro: "))
           acum1 = acum1 + cantidad
           opc1= int(input("Introduzca su opcion: "))
        print(f"El total vendido este domingo fue: {acum1} y los clientes que compraron fueron : {cont1}")
        print("Ha salido exitosamente")
 
   elif opc== 2:
       print(""""****Venta Segundo Domingo*******
          1. Registrar Venta
          2. Salir """)
       opc2= int(input("Introduzca su opcion: "))
       while opc2 == 1:
          nombre= input("Ingrese nombre del cliente: ")
          cont2 += 1
          cantidad= int(input("Ingrese la cantidad de nacatamales que compro: "))
          acum2 = acum2 + cantidad
          opc2= int(input("Introduzca su opcion: "))
       print(f"El total vendido este domingo fue: {acum2} y los clientes que compraron fueron : {cont2}")
       print("Ha salido exitosamente")
    
   elif opc== 3:
       print(""""****Venta Tercer Domingo*******
          1. Registrar Venta
          2. Salir """)
       opc3= int(input("Introduzca su opcion: "))
       while opc3 == 1:
          nombre= input("Ingrese nombre del cliente: ")
          cont3 += 1
          cantidad= int(input("Ingrese la cantidad de nacatamales que compro: "))
          acum3 = acum3 + cantidad
          opc3= int(input("Introduzca su opcion: "))
       print(f"El total vendido este domingo fue: {acum3} y los clientes que compraron fueron : {cont3}")
       print("Ha salido exitosamente")

   elif opc == 4:
       print(""""****Venta Cuarto Domingo*******
          1. Registrar Venta
          2. Salir """)
       opc4= int(input("Introduzca su opcion: "))
       while opc4 == 1:
          nombre= input("Ingrese nombre del cliente: ")
          cont4 += 1
          cantidad= int(input("Ingrese la cantidad de nacatamales que compro: "))
          acum4 = acum4 + cantidad
          opc4= int(input("Introduzca su opcion: "))
       print(f"El total vendido este domingo fue: {acum4} y los clientes que compraron fueron : {cont4}")
       print("Ha salido exitosamente")
   elif opc== 5:
     total_acum= acum1 + acum2 + acum3 + acum4
     total_clientes= cont1 + cont2 + cont3 + cont4  
     print(f"""$VENTAS DEL MES$
           Total Vendido : {total_acum}
           Total de Clientes: {total_clientes}
           ¡Gracias por confiar en nosotros! """) 
   else:
     print("Ha salido exitosamente del programa")
     break
