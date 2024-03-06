import storage.pedido as pe

def getAllEstadosDePedido():
    EstadoPedido = []
    for val in pe.pedido:
        EstadoPedido.append({
            "codigo_pedido": val.get("codigo_pedido"),
            "estado_pedido":val.get("estado"),
            "comentario": val.get("comentario")

        })
        
    return EstadoPedido