from datetime import datetime
from tabulate import tabulate
import requests


def getAllPedido():
    #json-server storage/pedido.json -b 4507 
    peticionPE= requests.get("http://172.16.106.98:4507")
    dataPE= peticionPE.json()
    return dataPE
def getPedidoCodigo(codigo):
    peticion= requests.get(f"http://172.16.106.98:4507/pedido/{codigo}")
    return[peticion.json()] if peticion.ok else []
def getAllEstadosDePedido():
    EstadoPedido = []
    for val in getAllPedido():
        EstadoPedido.append({
            "codigo_pedido": val.get("codigo_pedido"),
            "estado_pedido":val.get("estado"),
            "comentario": val.get("comentario")

        })
        
    return EstadoPedido

#devuelve un listado con el codigo de pedido codigo cl, fecha esperada y fecha de entrega de los pedidos que no han sido entrregados a tiempo

def getAllCodigoEsperadaEntregaPedido():
    codigoEstadoPedido = []
    for val in getAllPedido():
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

def getAllEstadosDePedido2009():
    Pedidosrechazados2009 = []
    for val in getAllPedido():
        if val.get("fecha_pedido").startswith("2009") and val.get("estado")=="Rechazado":

            Pedidosrechazados2009.append({
            "fecha_pedido": val.get("fecha_pedido"),
            "codigo_pedido": val.get("codigo_pedido"),
            "estado_pedido":val.get("estado"),
            "comentario": val.get("comentario")

        })
    # Pedidosrechazados2009.sort(datetime.strptime("fecha_pedido", "%d/%m/%Y"), reverse = True)
    Pedidosrechazados2009.sort(key=lambda x: datetime.strptime(x["fecha_pedido"], "%Y-%m-%d"), reverse=True) 
    return Pedidosrechazados2009

#devuelve un listado con el codigo de pedido, codigo cliente, fecha esperada, y fecha de entrega de los pedidos cuya feha de entrega ha sido al menos dos dias antes de la fecha esperada
def getAllpedidosDosDiasFechaEsperada():
    pedidosDosDiasFecha= []
    for val in getAllPedido():
        if val.get("estado") == "Entregado" and val.get("fecha_entrega") is None:
            val["fecha_entrega"] = val.get("fecha_esperada")
        if val.get("estado") == "Entregado":
            date_1 = "/".join(val.get("fecha_esperada").split("-")[::-1])
            date_2 = "/".join(val.get("fecha_entrega").split("-")[::-1])
            start= datetime.strptime(date_2, "%d/%m/%Y")
            end = datetime.strptime(date_1, "%d/%m/%Y")
            diff1 = end.date() - start.date()              
            if(diff1.days >= 2):
                pedidosDosDiasFecha.append({
                "codigo_pedido": val.get("codigo_pedido"),
                "estado_pedido":val.get("estado"),
                "fecha_entrega":val.get("fecha_entrega"),
                "comentario": val.get("comentario")

                                        })
        
    return pedidosDosDiasFecha

#devuelve un pedido de todos los pedidos que han sido entregados en cualquier ano en enero

def PedidosEntregadosEnero():
    PedidosEnero= []
    for val in getAllPedido():
        if val.get("estado")=="Entregado" and val.get("fecha_entrega") is not None:
            fecha_entrega = datetime.strptime(val.get("fecha_entrega"), "%Y-%m-%d")
            if fecha_entrega.month == 1:
                PedidosEnero.append({
            "codigo_pedido": val.get("codigo_pedido"),
            "estado_pedido":val.get("estado"),
            "fecha_entrega":val.get("fecha_entrega"),
            "comentario": val.get("comentario")

        })
    return PedidosEnero

def menu():
    while True:
        print("""
            

        _______ ____                ____           ___     __          
    / ____(_) / /__________     / __ \___  ____/ (_)___/ /___  _____
    / /_  / / / __/ ___/ __ \   / /_/ / _ \/ __  / / __  / __ \/ ___/
    / __/ / / / /_/ /  / /_/ /  / ____/  __/ /_/ / / /_/ / /_/ (__  ) 
    /_/   /_/_/\__/_/   \____/  /_/    \___/\__,_/_/\__,_/\____/____/  
                                                                    

            0. Regresar
            1. Obtener el estado del pedido
            2. Obtener un listado del cliente con los pedidos que no han sido enrtregados a tiempo
            3. Obtener un listado con todos los pedidos rechazados en 2009
            4. Pedidos entregados al menos dos dias antes de lo esperado
            5. Pedidos entregados en Enero
            
            """)
        opcion=int(input("Elija una de las opciones: "))
        
        
        if(opcion==1):
            print(tabulate(getAllEstadosDePedido(), headers="keys", tablefmt = 'rounded_grid'))
        
        elif(opcion==2):
            print(tabulate(getAllCodigoEsperadaEntregaPedido(), headers="keys", tablefmt = 'rounded_grid'))    
        
        elif(opcion == 3):
            print(tabulate(getAllEstadosDePedido2009(), headers="keys", tablefmt='rounded_grid'))

        elif(opcion == 4):
            print(tabulate(getAllpedidosDosDiasFechaEsperada(), headers="keys", tablefmt='rounded_grid'))    
       
        elif(opcion==5):
            print(tabulate(PedidosEntregadosEnero(), headers="keys", tablefmt='rounded_grid'))
        
        elif(opcion==0):
            break