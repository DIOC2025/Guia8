#Control de ventas en kioscos estudiantiles de la UAM
producto1_k1= producto2_k1= producto3_k1= producto4_k1= producto5_k1= 0
producto1_k2=producto2_k2=producto3_k2=producto4_k2= producto5_k2= 0
producto1_k3= producto2_k3= producto3_k3= producto4_k3= producto5_k3= 0
total_kiosko1= total_kiosko2= total_kiosko3= 0

while True:
   print("*************************BIENVENIDOS A  LOS KIOSKOS*******************")
   print("""Elija una opción
      1. Primer Kiosko
      2. Segundo Kiosko
      3. Tercer Kiosko
      4. Salir""")
   opc= int(input("Introduzca su opcion: "))

   if opc == 1:
    while True: 
        print(""""****Venta Primer kiosko*******
          1. Producto 1
          2. Producto 2
          3. Producto 3
          4. Producto 4
          5. Producto 5
          6. Salir """)
        opc1= int(input("Introduzca su opcion: "))
        cantidad= int(input ("Ingrese la cantidad"))
        
        if opc1==1:
           producto1_k1 += cantidad
        elif opc1== 2:
           producto2_k1 += cantidad
        elif opc1 == 3:
           producto3_k1 += cantidad
        elif opc1 == 4:
           producto4_k1 += cantidad
        elif opc1 == 5:
           producto5_k1 += cantidad
        else:
           total_kiosko1= producto1_k1 + producto2_k1 + producto3_k1 + producto4_k1 + producto5_k1
           print(f""" Ventas Producto 1: {producto1_k1}
                 Ventas Producto 2: {producto2_k1}
                 Ventas Producto 3: {producto3_k1}
                 Ventas Producto 4: {producto4_k1}
                 Ventas Producto 5: {producto5_k1}
                 Ventas Total del dia: {total_kiosko1} """)
           break
        
   if opc == 2:
      while True: 
        print(""""****Venta Segundo Kiosko****
          1. Producto 1
          2. Producto 2
          3. Producto 3
          4. Producto 4
          5. Producto 5
          6. Salir """)
        opc2= int(input("Introduzca su opcion: "))
        cantidad= int(input ("Ingrese la cantidad"))
        
        if opc2==1:
           producto1_k2+= cantidad
        elif opc2== 2:
           producto2_k2+= cantidad
        elif opc2 == 3:
           producto3_k2+= cantidad
        elif opc2 == 4:
           producto4_k2+= cantidad
        elif opc2 == 5:
           producto5_k2 += cantidad
        else:
           total_kiosko2= producto1_k2 + producto2_k2 + producto3_k2 + producto4_k2 + producto5_k2
           print(f""" Ventas Producto 1: {producto1_k2}
                 Ventas Producto 2: {producto2_k2}
                 Ventas Producto 3: {producto3_k2}
                 Ventas Producto 4: {producto4_k2}
                 Ventas Producto 5: {producto5_k2}
                 Ventas Total del dia: {total_kiosko2} """)
           break

   elif  opc== 3:
      while True: 
        print(""""****Venta Tercer Kiosko****
          1. Producto 1
          2. Producto 2
          3. Producto 3
          4. Producto 4
          5. Producto 5
          6. Salir """)
        opc3= int(input("Introduzca su opcion: "))
        cantidad= int(input ("Ingrese la cantidad"))
        
        if opc3==1:
           producto1_k3 += cantidad
        elif opc3== 2:
           producto2_k3 += cantidad
        elif opc3 == 3:
           producto3_k3 += cantidad
        elif opc3 == 4:
           producto4_k3 += cantidad
        elif opc3 == 5:
           producto5_k3 += cantidad
        else:
           total_kiosko3= producto1_k3 + producto2_k3 + producto3_k3 + producto4_k3 + producto5_k3
           print(f""" Ventas Producto 1: {producto1_k3}
                 Ventas Producto 2: {producto2_k3}
                 Ventas Producto 3: {producto3_k3}
                 Ventas Producto 4: {producto4_k3}
                 Ventas Producto 5: {producto5_k3}
                 Ventas Total del dia: {total_kiosko3} """)
           break
    
   else:
       print("Ha salido exitosamente del programa")
       break
