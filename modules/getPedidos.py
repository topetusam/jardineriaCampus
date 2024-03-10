import storage.pedido as pe
from datetime import datetime

def getAllEstadosDePedido():
    EstadoPedido = []
    for val in pe.pedido:
        EstadoPedido.append({
            "codigo_pedido": val.get("codigo_pedido"),
            "estado_pedido":val.get("estado"),
            "comentario": val.get("comentario")

        })
        
    return EstadoPedido

#devuelve un listado con el codigo de pedido codigo cl, fecha esperada y fecha de entrega de los pedidos que no han sido entrregados a tiempo

def getAllCodigoEsperadaEntregaPedido():
    codigoEstadoPedido = []
    for val in pe.pedido:
        if val.get("estado")=="Entregado" and val.get("fecha_entrega") is None:
            val["fecha_entrega"] = val.get("fecha_esperada")
        if val.get("estado") == "Entregado":
            date_1 = "/".join(val.get("fecha_esperada").split("-")[::-1])
            date_2 = "/".join(val.get("fecha_entrega").split("-")[::-1])
            start= datetime.strptime(date_2, "%d/%m/%Y")
            end = datetime.strptime(date_1, "%d/%m/%Y")
            diff = end.date() - start.date()              
            if(diff.days <0):
                codigoEstadoPedido.append({
                "codigo_pedido": val.get("codigo_pedido"),
                "estado_pedido":val.get("estado"),
                "fecha_entrega":val.get("fecha_entrega"),
                "comentario": val.get("comentario")

                                        })
        
    return codigoEstadoPedido



#devuelve un listado de todos los pedidos rechazados en 2009


def menu():
    print("""
          
          1. Obtener todos los clientes (nombre)
          2. Obtener un cliente por el codigo
          3. Obtener toda la informacion del cliente segun su limite de credito y ciudad que pertenece
          4. Obtener clientes por pais, region y ciudad
          5. Obtener cliente por pais
          
          """)
    opcion=int(input("Elija una de las opciones: "))
    
    
    if(opcion==1):
        print(tabulate(searchAllClientesName(), headers="keys", tablefmt = 'rounded_grid'))
    
    elif(opcion==2):
        codigoCliente= int(input("Ingrese el codigo del cliente: "))
        print(tabulate(getoneClientecodigo(codigoCliente), headers="keys", tablefmt = 'rounded_grid'))    
    
    elif(opcion == 3):
        limiteCredit = int(input("Ingrese el limite de credito de los clientes que deseas visualizar: "))
        ciudad = input("ingrese la ciudad que desea filtrar los clientes: ")
        print(tabulate(getAllClientCreditCiudad(limiteCredit, ciudad), headers="keys", tablefmt='rounded_grid'))