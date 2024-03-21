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

    peticion= requests.post(" http://154.38.171.54:5003/empleados", data=json.dumps(empleado))
    res = peticion.json()
    res["mensaje"]="Producto Guardado"
    return [res]

def updateEmpleado(id):
    empleado = {
        "codigo_empleado": int(input("Ingrese el nuevo codigo del empleado: ")),
        "nombre": input("Ingrese el nuevo nombre: "),
        "apellido1": input("Ingrese el nuevo apellido1: "),
        "apellido2": input("Ingrese el nuevo apellido2: "),
        "extension": input("Ingrese la nueva extension: "),
        "email": input("Ingrese el nuevo email: "),
        "codigo_oficina": input("Ingrese el nuevo codigo de la oficina: "),
        "codigo_jefe": int(input("Ingrese el nuevo codigo del jefe: ")),
        "puesto": input("Ingrese el nuevo puesto del empleado: ")
    }

    empleado_existente = gE.getEmpleadoCodigo(id)
    if not empleado_existente:
        return {"mensaje": "Producto no encontrado"}

    empleado_actualizado = {**empleado_existente[0], **empleado}


    peticion = requests.put(f" http://154.38.171.54:5003/empleados/{id}", data=json.dumps(empleado_actualizado))
    res = peticion.json()

    if peticion.status_code == 200:
        res["mensaje"] = "Producto actualizado correctamente"
    else:
        res["mensaje"] = "Error al actualizar el producto"
    
    return [res]



def deleteEmpleado(id):
    data = gE.getEmpleadoCodigo(id)
    if(len(data)):
        peticion = requests.delete(f" http://154.38.171.54:5003/empleados/{id}")
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

def menu2():
    
    while True:
        print("""  
                                              
                                                                                                                                                    
            1. Actualizar un Empleado
            0. Atras
          
          """)        
        opcion = int(input("\nSelecione una de las opciones: "))
        if(opcion == 1):
            id = input("Ingrese el id del Empleado que desea actualizar: ")
            print(tabulate(updateEmpleado(id), headers="keys", tablefmt="github"))
            input("Precione una tecla para continuar.....")
        elif(opcion == 0):
            break