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
        "codigo_cliente_rep_ventas": int(input("Ingrese el codigo del empledo rep ventas: ")),
        "limite_credito": int(input("Ingrese el limite de credito: "))

    }

    peticion= requests.post("http://172.16.106.53:4503/cliente", data=json.dumps(cliente))
    res = peticion.json()
    res["mensaje"]="Producto Guardado"
    return [res]

def updateCliente(id):
    cliente = {
        "codigo_cliente": int(input("Ingrese el nuevo codigo del cliente: ")),
        "nombre_cliente": input("Ingrese el nuevo nombre del cliente: "),
        "nombre_contacto": input("Ingrese el nuevo nombre del contacto: "),
        "apellido_contacto": input("Ingrese el nuevo apellido del contacto: "),
        "telefono": input("Ingrese el nuevo telefono: "),
        "fax": input("Ingrese el nuevo fax: "),
        "linea_direccion1": input("Ingrese la nueva direccion 1: "),
        "linea_direccion2": input("Ingrese la nueva direccion 2: "),
        "ciudad": input("Ingrese la nueva ciudad: "),
        "region": input("Ingrese la nueva region: "),
        "pais": input("Ingrese el nuevo pais: "),
        "codigo_postal": input("Ingrese el nuevo codigo postal: "),
        "codigo_cliente_rep_ventas": int(input("Ingrese el nuevo codigo del empledo rep ventas: ")),
        "limite_credito": int(input("Ingrese el nuevo limite de credito: "))
    }

    cliente_existente = gC.getClienteCodigo(id)
    if not cliente_existente:
        return {"mensaje": "Producto no encontrado"}

    cliente_actualizado = {**cliente_existente[0], **cliente}


    peticion = requests.put(f"http://172.16.106.53:4503/cliente/{id}", data=json.dumps(cliente_actualizado))
    res = peticion.json()

    if peticion.status_code == 200:
        res["mensaje"] = "Producto actualizado correctamente"
    else:
        res["mensaje"] = "Error al actualizar el producto"
    
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
def menu2():
    
    while True:
        print("""  
                                                                                     
            1. Actualizar un Cliente
            0. Atras
          
          """)        
        opcion = int(input("\nSelecione una de las opciones: "))
        if(opcion == 1):
            id = input("Ingrese el id del Cliente que desea actualizar: ")
            print(tabulate(updateCliente(id), headers="keys", tablefmt="github"))
            input("Precione una tecla para continuar.....")
        elif(opcion == 0):
            break