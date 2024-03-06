from tabulate import tabulate


import modules.getClient as cliente
import modules.getOficina as oficina
import modules.getEmpleados as empleado

print(tabulate(empleado.getAllNombreApellidoEmailJefe(7), tablefmt = 'grid'))


