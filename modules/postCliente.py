import os 
from tabulate import tabulate
import json
import requests
import modules.getGama as gG


def postCliente():
    cliente={ 
     "codigo_cliente": int(input("Ingrese el codigo del cliente: ")),
        "nombre_cliente": input("Ingrese el nombre del cliente: "),
        "nombre_contacto": input("Ingrese el nombre del contacto: "),
        "apellido_contacto": input("Ingrese el apellido del contacto: "),
        "telefono": input("Ingrese el telefono: "),
        "fax": input("Ingrese el fax: "),
        "linea_direccion1": input("Ingrese la direccion 1: "),
        "linea_direccion2": input("Ingrese la direccion 2: "),
        "ciudad": input("Ingrese la ciudad: "),
        "region": input("Ingrese la region: "),
        "pais": input("Ingrese el pais: "),
        "codigo_postal": input("Ingrese el codigo postal: "),
        "codigo_empleado_rep_ventas": int(input("Ingrese el codigo del empledo rep ventas: ")),
        "limite_credito": int(input("Ingrese el limite de credito: "))

    }

    peticion= requests.post("http://172.16.106.105:4503", data=json.dumps(cliente))
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
            print(tabulate(postCliente(), headers="keys", tablefmt="github"))
            input("Precione una tecla para continuar.....")
        elif(opcion == 0):
            break
