from tabulate import tabulate

import modules.getClient as cliente
import modules.getOficina as oficina
import modules.getEmpleados as empleado
import modules.getPago as pago
import modules.getPedidos as pedido



#print(tabulate(empleado.getAllNombreApellidoEmailJefe(3), tablefmt = 'grid'))

print(tabulate(pago.getAllFechaPago(), tablefmt='grid'))



