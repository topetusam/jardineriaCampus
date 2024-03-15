from tabulate import tabulate

import modules.getClient as cliente
import modules.getOficina as oficina
import modules.getEmpleados as empleado
import modules.getPago as pago
import modules.getPedidos as pedido
import modules.getProducto as rrproducto
import modules.postProducto as PProducto
import os 





#print(tabulate(empleado.getAllNombreApellidoEmailJefe(3), tablefmt = 'grid'))
# print(tabulate(cliente.clientesCiudadMadrid(), tablefmt='grid'))
def menuProducto():
    while True:
        os.system("clear")
        print("""
              
    ____  _                            _     __               __                                 
   / __ )(_)__  ____ _   _____  ____  (_)___/ /___     ____ _/ /  ____ ___  ___  ____  __  __    
  / __  / / _ \/ __ \ | / / _ \/ __ \/ / __  / __ \   / __ `/ /  / __ `__ \/ _ \/ __ \/ / / /    
 / /_/ / /  __/ / / / |/ /  __/ / / / / /_/ / /_/ /  / /_/ / /  / / / / / /  __/ / / / /_/ /     
/_____/_/\___/_/ /_/|___/\___/_/ /_/_/\__,_/\____/ __\__,_/_/  /_/ /_/ /_/\___/_/ /_/\__,_/      
  ____/ /__     ____  _________  ____/ /_  _______/ /_____  _____                                
 / __  / _ \   / __ \/ ___/ __ \/ __  / / / / ___/ __/ __ \/ ___/                                
/ /_/ /  __/  / /_/ / /  / /_/ / /_/ / /_/ / /__/ /_/ /_/ (__  )                                 
\__,_/\___/  / .___/_/   \____/\__,_/\__,_/\___/\__/\____/____/                                  
            /_/                                                                                  
        
            1. Reportes de los productos
            2. Guardar, Actualizar y Eliminar productos
            0. Regresar al menu principal
          
            """)
        opcion = int(input("\nSelecione una de las opciones: "))
        if(opcion == 1):
            rrproducto.menu()
        if(opcion == 2):
            PProducto.menu()
        elif(opcion == 0):
            break

if (__name__=='__main__'):
    while True:
            print("""

       
    __  ___                    ____       _            _             __
   /  |/  /__  ____  __  __   / __ \_____(_)___  _____(_)___  ____ _/ /
  / /|_/ / _ \/ __ \/ / / /  / /_/ / ___/ / __ \/ ___/ / __ \/ __ `/ / 
 / /  / /  __/ / / / /_/ /  / ____/ /  / / / / / /__/ / /_/ / /_/ / /  
/_/  /_/\___/_/ /_/\__,_/  /_/   /_/  /_/_/ /_/\___/_/ .___/\__,_/_/   
                                                    /_/                
   
          0. Salir
          1. Cliente
          2. Oficina
          3. Empleados
          4. Pago
          5. Pedidos 
          6. producto
          
          """)
            opcion = int(input("\n Seleccione unas de las opciones: "))
            
            if(opcion==1):
                cliente.menu()
            elif(opcion==2):
                oficina.menu()
            elif(opcion==3):
                empleado.menu()
            elif(opcion==4):
                pago.menu()
            elif(opcion==5):
                pedido.menu()
            elif(opcion==6):
                menuProducto()  
            elif(opcion==0):
                break           
    
            # try:
            #      opcion = int(input("\n Seleccione unas de las opciones: "))
            
            # except ValueError as error:
            #      print("Error generado"+error)

            
                 
            
            # finally:



            # if(opcion==1):
            #     cliente.menu()
            # elif(opcion==2):
            #     oficina.menu()
            # elif(opcion==3):
            #     empleado.menu()
            # elif(opcion==4):
            #     pago.menu()
            # elif(opcion==5):
            #     pedido.menu()
            # elif(opcion==6):
            #     menuProducto()  
            # elif(opcion==0):
            #     break           
    