import os 
from tabulate import tabulate
import json
import requests
import modules.getOficina as gO


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

    peticion= requests.post("http://172.16.106.53:4506/oficina", data=json.dumps(oficina))
    res = peticion.json()
    res["mensaje"]="Producto Guardado"
    return [res]
def deleteOficina(id):
    data = gO.getOficinaCodigo(id)
    if(len(data)):
        peticion = requests.delete(f"http://172.16.106.53:4501/oficina/{id}")
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
            print(tabulate(postOficina(), headers="keys", tablefmt="github"))
            input("Precione una tecla para continuar.....")
        elif(opcion == 0):
            break
def menu1():
    while True:
        print("""  
                                            
                                                                                                                                                    
            1. Eliminar una Oficina
            0. Atras
          
          """)        
        opcion = int(input("\nSelecione una de las opciones: "))
        if(opcion == 1):
            idOficina = input("Ingrese el id de la oficina que desea eliminar: ")
            print(tabulate(deleteOficina(idOficina)["body"], headers="keys", tablefmt="github"))

            input("Precione una tecla para continuar.....")
        elif(opcion == 0):
            break
