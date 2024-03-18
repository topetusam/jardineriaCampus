import os 
from tabulate import tabulate
import json
import requests
import modules.getGama as gG


def postOficina():
    oficina = {
        "codigo_oficina": input("Ingrese el codigo de la oficina: "),
        "ciudad": input("Ingrese la ciudad: "),
        "pais": input("Ingrese el pais: "),
        "region": input("Ingrese la region: "),
        "codigo_postal": input("Ingrese el codigo postal: "),
        "telefono": input("Ingrese el telefono: "),
        "linea_direccion1": input("Ingrese la direccion1: "),
        "linea_direccion2": input("Ingrese la direccion2: ")
    }

    peticion= requests.post("http://172.16.106.105:4506", data=json.dumps(oficina))
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
            print(tabulate(postOficina(), headers="keys", tablefmt="github"))
            input("Precione una tecla para continuar.....")
        elif(opcion == 0):
            break
