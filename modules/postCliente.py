import os 
from tabulate import tabulate
import json
import requests
import modules.getClient as gC


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

    peticion= requests.post("http://172.16.106.53:4503/cliente", data=json.dumps(cliente))
    res = peticion.json()
    res["mensaje"]="Producto Guardado"
    return [res]
def deleteCliente(id):
    data = gC.getClienteCodigo(id)
    if(len(data)):
        peticion = requests.delete(f"http://172.16.106.53:4501/cliente/{id}")
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
            print(tabulate(postCliente(), headers="keys", tablefmt="github"))
            input("Precione una tecla para continuar.....")
        elif(opcion == 0):
            break
def menu1():
    while True:
        print("""                                                                                                                                             
            1. Eliminar un Cliente
            0. Atras
          
          """)        
        opcion = int(input("\nSelecione una de las opciones: "))
        if(opcion == 1):
            idCliente = input("Ingrese el id del cliente que desea eliminar: ")
            print(tabulate(deleteCliente(idCliente)["body"], headers="keys", tablefmt="github"))

            input("Precione una tecla para continuar.....")
        elif(opcion == 0):
            break
