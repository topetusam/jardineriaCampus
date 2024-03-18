import os 
from tabulate import tabulate
import json
import requests
import modules.getGama as gG


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

    peticion= requests.post("http://172.16.106.105:4507", data=json.dumps(pedido))
    res = peticion.json()
    res["mensaje"]="Producto Guardado"
    return [res]

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
