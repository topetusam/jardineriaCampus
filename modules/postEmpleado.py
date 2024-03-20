import os 
from tabulate import tabulate
import json
import requests
import modules.getEmpleados as gE


def postEmpleado():
    empleado = {
        "codigo_empleado": int(input("Ingrese el codigo del empleado: ")),
        "nombre": input("Ingrese el nombre: "),
        "apellido1": input("Ingrese el apellido1: "),
        "apellido2": input("Ingrese el apellido2: "),
        "extension": input("Ingrese la extension: "),
        "email": input("Ingrese el email: "),
        "codigo_oficina": input("Ingrese el codigo de la oficina: "),
        "codigo_jefe": int(input("Ingrese el codigo del jefe: ")),
        "puesto": input("Ingrese el puesto del empleado: ")
    }

    peticion= requests.post("http://172.16.106.98:4504", data=json.dumps(empleado))
    res = peticion.json()
    res["mensaje"]="Producto Guardado"
    return [res]
def deleteEmpleado(id):
    data = gE.getEmpleadoCodigo(id)
    if(len(data)):
        peticion = requests.delete(f"http://172.16.106.98:4501/empleado/{id}")
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
            print(tabulate(postEmpleado(), headers="keys", tablefmt="github"))
            input("Precione una tecla para continuar.....")
        elif(opcion == 0):
            break
def menu1():
    while True:
        print("""  
                                               
                                                                                                                                                    
            1. Eliminar un Empleado
            0. Atras
          
          """)        
        opcion = int(input("\nSelecione una de las opciones: "))
        if(opcion == 1):
            idEmpleado = input("Ingrese el id del Empleado que desea eliminar: ")
            print(tabulate(deleteEmpleado(idEmpleado)["body"], headers="keys", tablefmt="github"))

            input("Precione una tecla para continuar.....")
        elif(opcion == 0):
            break
