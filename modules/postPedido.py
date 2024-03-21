import os 
from tabulate import tabulate
import json
import requests
import modules.getPedidos as gPe


def postPedido():
    pedido = {
        "codigo_pedido": int(input("Ingrese el codigo del pedido: ")),
        "fecha_pedido": input("Ingrese la fecha del pedido: "),
        "fecha_esperada": input("Ingrese la fecha esperada: "),
        "fecha_entrega": input("Ingrese la fecha de entrega: "),
        "estado": input("Ingrese el estado del pedido: "),
        "comentario": input("Ingrese un comentario: "),
        "codigo_cliente": int(input("Ingrese el codigo del cliente: "))
    }

    peticion= requests.post(" http:// http://154.38.171.54:5007/pedidos", data=json.dumps(pedido))
    res = peticion.json()
    res["mensaje"]="Producto Guardado"
    return [res]


def updatePedido(id):
    pedido = {
       "codigo_pedido": int(input("Ingrese el nuevo codigo del pedido: ")),
        "fecha_pedido": input("Ingrese la nueva fecha del pedido: "),
        "fecha_esperada": input("Ingrese la nueva fecha esperada: "),
        "fecha_entrega": input("Ingrese la nueva fecha de entrega: "),
        "estado": input("Ingrese el nuevo estado del pedido: "),
        "comentario": input("Ingrese un nuevo comentario: "),
        "codigo_cliente": int(input("Ingrese el nuevo codigo del cliente: "))
    }

    pedido_existente = gPe.getPedidoCodigo(id)
    if not pedido_existente:
        return {"mensaje": "Producto no encontrado"}

    pedido_actualizado = {**pedido_existente[0], **pedido}


    peticion = requests.put(f" http:// http://154.38.171.54:5007/pedidos/{id}", data=json.dumps(pedido_actualizado))
    res = peticion.json()

    if peticion.status_code == 200:
        res["mensaje"] = "Producto actualizado correctamente"
    else:
        res["mensaje"] = "Error al actualizar el producto"
    
    return [res]





def deletePedido(id):
    data = gPe.getPedidoCodigo(id)
    if(len(data)):
        peticion = requests.delete(f" http:// http://154.38.171.54:5007/pedidos/{id}")
        if(peticion.status_code == 204):
            data.append({"message": "producto eliminado correctamente"})
            return {
                "body": data, 
                "status": peticion.status_code,
            }
    else:
        return {
            "body":[{
                "message":"producto no encontrado",
                "id": id
            }],
            "status": 400,
        }


    pedido = {
        "codigo producto": input("Ingrese el nuevo código del producto: "),
        "nombre producto": input("Ingrese el nuevo nombre del producto: "),
        "gama_producto": input("Ingrese la nueva gama del producto: "),
        "descripcion producto": input("Ingrese la nueva descripción del producto: "),
        "Dimensiones": input("Ingrese la nueva dimensión: "),
        "Proveedor": input("Ingrese el nuevo proveedor: "),
        "cantidad_en_stock": int(input("Ingrese el nuevo stock del producto: ")),
        "precio_venta": int(input("Ingrese el nuevo precio de venta: ")),
        "precio_proveedor": int(input("Ingrese el nuevo precio del proveedor: "))
    }

    peticion = requests.put(f" http:// http://154.38.171.54:5007/pedidos/{id}", data=json.dumps(pedido))
    res = peticion.json()
    if peticion.status_code == 200:
        res["mensaje"] = "Pedido actualizado correctamente"
        res["id"]= id
    else:
        res["mensaje"] = "Error al actualizar el pedido"
    return [res]



def menu():
    while True:
        print("""  
                                             
                                                                                                                                                    
            1. Guardar un pedido nuevo
            0. Atras
          
          """)        
        opcion = int(input("\nSelecione una de las opciones: "))
        if(opcion == 1):
            print(tabulate(postPedido(), headers="keys", tablefmt="github"))
            input("Precione una tecla para continuar.....")
        elif(opcion == 0):
            break
def menu1():
    while True:
        print("""  
                                                
                                                                                                                                                    
            1. Eliminar un Pedido
            0. Atras
          
          """)        
        opcion = int(input("\nSelecione una de las opciones: "))
        if(opcion == 1):
            idPedido = input("Ingrese el id del pedido que desea eliminar: ")
            print(tabulate(deletePedido(idPedido)["body"], headers="keys", tablefmt="github"))

            input("Precione una tecla para continuar.....")
        elif(opcion == 0):
            break
def menu2():

    while True:
        print("""                                                
                                                                                                                                                    
            1. Actualizar un Pedido
            0. Atras
          
          """)        
        opcion = int(input("\nSelecione una de las opciones: "))
        if(opcion == 1):
            id = input("Ingrese el id del pedido que desea actualizar: ")
            print(tabulate(updatePedido(id), headers="keys", tablefmt="github"))
            input("Precione una tecla para continuar.....")
        elif(opcion == 0):
            break