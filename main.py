from tabulate import tabulate

import modules.getClient as cliente
import modules.getOficina as oficina
import modules.getEmpleados as empleado
import modules.getPago as pago
import modules.getPedidos as pedido



#print(tabulate(empleado.getAllNombreApellidoEmailJefe(3), tablefmt = 'grid'))

print(tabulate(pedido.getAllCodigoEsperadaEntregaPedido(), tablefmt='grid'))


if (__name__=='__main__'):
    print("""
          
          
          1. Cliente
          2. Oficina
          3. Empleados
          4. Pedidos
          5.Pagos 
          
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
        
