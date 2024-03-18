import os 
from tabulate import tabulate
import json
import requests
import modules.getGama as gG


def postPago():
    pago = {
        "codigo_cliente": int(input("Ingrese el codigo del cliente: ")),
        "forma_pago": input("Ingrese la forma de pago: "),
        "id_transaccion": input("Ingrese el id de la transaccion: "),
        "fecha_pago": input("Ingrese la fecha del pago: "),
        "total": int(input("Ingrese el total: "))
    }

    peticion= requests.post("http://172.16.106.89:4505", data=json.dumps(pago))
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
            print(tabulate(postPago(), headers="keys", tablefmt="github"))
            input("Precione una tecla para continuar.....")
        elif(opcion == 0):
            break
