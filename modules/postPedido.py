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

    peticion= requests.post("http://172.16.106.53:4507/pedido", data=json.dumps(pedido))
    res = peticion.json()
    res["mensaje"]="Producto Guardado"
    return [res]

def deletePedido(id):
    data = gPe.getPedidoCodigo(id)
    if(len(data)):
        peticion = requests.delete(f"http://172.16.106.53:4501/pedido/{id}")
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

def menu():
    while True:
        print("""  
                                             
                                                                                                                                                    
            1. Guardar un producto nuevo
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
