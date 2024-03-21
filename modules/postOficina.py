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

    peticion= requests.post(" http://154.38.171.54:5005/oficinas ", data=json.dumps(oficina))
    res = peticion.json()
    res["mensaje"]="Producto Guardado"
    return [res]

def updateOficina(id):
    oficina = {
        "codigo_oficina": input("Ingrese el nuevo codigo de la oficina: "),
        "ciudad": input("Ingrese la nueva ciudad: "),
        "pais": input("Ingrese el nuevo pais: "),
        "region": input("Ingrese la nueva region: "),
        "codigo_postal": input("Ingrese el nuevo codigo postal: "),
        "telefono": input("Ingrese el nuevo telefono: "),
        "linea_direccion1": input("Ingrese la nueva direccion1: "),
        "linea_direccion2": input("Ingrese la nueva direccion2: ")
    }

    oficina_existente = gO.getOficinaCodigo(id)
    if not oficina_existente:
        return {"mensaje": "Producto no encontrado"}

    oficina_actualizado = {**oficina_existente[0], **oficina}


    peticion = requests.put(f"http://154.38.171.54:5005/oficinas /{id}", data=json.dumps(oficina_actualizado))
    res = peticion.json()

    if peticion.status_code == 200:
        res["mensaje"] = "Producto actualizado correctamente"
    else:
        res["mensaje"] = "Error al actualizar el producto"
    
    return [res]







def deleteOficina(id):
    data = gO.getOficinaCodigo(id)
    if(len(data)):
        peticion = requests.delete(f"http://http://154.38.171.54:5005/oficinas/{id}")
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
def menu2():
    
    while True:
        print("""  
                                                
                                                                                                                                                    
            1. Actualizar una oficina
            0. Atras
          
          """)        
        opcion = int(input("\nSelecione una de las opciones: "))
        if(opcion == 1):
            id = input("Ingrese el id de la Oficina que desea actualizar: ")
            print(tabulate(updateOficina(id), headers="keys", tablefmt="github"))
            input("Precione una tecla para continuar.....")
        elif(opcion == 0):
            break