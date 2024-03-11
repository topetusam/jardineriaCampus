from tabulate import tabulate

import modules.getClient as cliente
import modules.getOficina as oficina
import modules.getEmpleados as empleado
import modules.getPago as pago
import modules.getPedidos as pedido



#print(tabulate(empleado.getAllNombreApellidoEmailJefe(3), tablefmt = 'grid'))

# print(tabulate(cliente.getAllClientePais("United Kingdom"), tablefmt='grid'))


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
            elif(opcion==0):
                break           
    
        
