import os 
from tabulate import tabulate
import json
import requests
import modules.getPago as gPa


def postPago():
    pago = {
        "codigo_cliente": int(input("Ingrese el codigo del cliente: ")),
        "forma_pago": input("Ingrese la forma de pago: "),
        "id_transaccion": input("Ingrese el id de la transaccion: "),
        "fecha_pago": input("Ingrese la fecha del pago: "),
        "total": int(input("Ingrese el total: "))
    }

    peticion= requests.post("http://172.16.106.53:4505/pago", data=json.dumps(pago))
    res = peticion.json()
    res["mensaje"]="Producto Guardado"
    return [res]



def updatePago(id):
    pago = {
        "codigo_cliente": int(input("Ingrese el nuevo codigo del cliente: ")),
        "forma_pago": input("Ingrese la nueva forma de pago: "),
        "id_transaccion": input("Ingrese el nuevo id de la transaccion: "),
        "fecha_pago": input("Ingrese la nueva fecha del pago: "),
        "total": int(input("Ingrese el nuevo total: "))
    }

    pago_existente = gPa.getPagoCodigo(id)
    if not pago_existente:
        return {"mensaje": "Producto no encontrado"}

    pago_actualizado = {**pago_existente[0], **pago}


    peticion = requests.put(f"http://172.16.106.53:4505/pago/{id}", data=json.dumps(pago_actualizado))
    res = peticion.json()

    if peticion.status_code == 200:
        res["mensaje"] = "Producto actualizado correctamente"
    else:
        res["mensaje"] = "Error al actualizar el producto"
    
    return [res]



def deletePago(id):
    
    data = gPa.getPagoCodigo(id)
    if(len(data)):
        peticion = requests.delete(f"http://172.16.106.53:4501/pago/{id}")
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
                                            
                                                                                                                                                    
            1. Guardar un pago nuevo
            0. Atras
          
          """)        
        opcion = int(input("\nSelecione una de las opciones: "))
        if(opcion == 1):
            print(tabulate(postPago(), headers="keys", tablefmt="github"))
            input("Precione una tecla para continuar.....")
        elif(opcion == 0):
            break
def menu1():
    while True:
        print("""  
                                                
                                                                                                                                                    
            1. Eliminar un Pago
            0. Atras
          
          """)        
        opcion = int(input("\nSelecione una de las opciones: "))
        if(opcion == 1):
            idPago = input("Ingrese el id del pago que desea eliminar: ")
            print(tabulate(deletePago(idPago)["body"], headers="keys", tablefmt="github"))

            input("Precione una tecla para continuar.....")
        elif(opcion == 0):
            break
def menu2():
    
    while True:
        print("""  
                                                
                                                                                                                                                    
            1. Actualizar un Pago
            0. Atras
          
          """)        
        opcion = int(input("\nSelecione una de las opciones: "))
        if(opcion == 1):
            id = input("Ingrese el id del pago que desea actualizar: ")
            print(tabulate(updatePago(id), headers="keys", tablefmt="github"))
            input("Precione una tecla para continuar.....")
        elif(opcion == 0):
            break