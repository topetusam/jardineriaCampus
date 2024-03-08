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


#devuelve un listado con el codigo de pedido  codigo cl, fecha esperada y fecha enrtrega de los  pedidos cuya fecha de entrega ha sido al menos dos dias antes de la fehca esperada
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


