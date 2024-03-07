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
# date_1='2006-01-17'
# date_2='2006-01-17'

# lista = "/".join("2006-01-19" .split("-")[::-1])    


def getAllCodigoEsperadaEntregaPedido():
    codigoEstadoPedido = []
    for val in pe.pedido:
        if val.get("estado")=="Entregado" and val.get("fecha_entrega") == None:
            val["fecha_entrega"]==val.get("fecha_esperada")
        if val.get("estado") == "Entregado":
            date_1 = "/".join(val.get("fecha_esperada").split("-")[::-1])
            date_2 = "/".join(val.get("fecha_entrega").split("-")[::-1])
            start= datetime.strptime(date_1, "%d/%m/%Y")
            end = datetime.strptime(date_2, "%d/%m/%Y")
            diff = end.date() - start.date()                        
            if(diff.days <0):
                codigoEstadoPedido.append({
                "codigo_pedido": val.get("codigo_pedido"),
                "estado_pedido":val.get("estado"),
                "fecha_entrega":val.get("fecha_entrega"),
                "comentario": val.get("comentario")

        })
        
    return codigoEstadoPedido






