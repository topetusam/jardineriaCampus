import os 
from tabulate import tabulate
import json
import requests
import modules.getGama as gGa


def postGama():
    gama = {

        "gama": input("Ingrese la gama del producto: "),
        "descripcion_texto": input("Ingrese la descripcion del producto: "),
        "descripcion_html": input("Ingrese la descripcion HTML: "),
        "imagen": input("Ingrese la url de la Imagen: ")
    }

    peticion= requests.post(" http://154.38.171.54:5004/gama", data=json.dumps(gama))
    res = peticion.json()
    res["mensaje"]="Producto Guardado"
    return [res]


def updateGama(id):
    gama = {
        "gama": input("Ingrese la nueva gama del producto: "),
        "descripcion_texto": input("Ingrese la nueva descripcion del producto: "),
        "descripcion_html": input("Ingrese la nueva descripcion HTML: "),
        "imagen": input("Ingrese la nueva url de la Imagen: ")
    }

    gama_existente = gGa.getGamaCodigo(id)
    if not gama_existente:
        return {"mensaje": "Producto no encontrado"}

    gama_actualizado = {**gama_existente[0], **gama}


    peticion = requests.put(f"http://154.38.171.54:5004/gama/{id}", data=json.dumps(gama_actualizado))
    res = peticion.json()

    if peticion.status_code == 200:
        res["mensaje"] = "Producto actualizado correctamente"
    else:
        res["mensaje"] = "Error al actualizar el producto"
    
    return [res]



def deleteGama(id):
    data = gGa.getGamaCodigo(id)
    if(len(data)):
        peticion = requests.delete(f" http://154.38.171.54:5004/gama/{id}")
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
            print(tabulate(postGama(), headers="keys", tablefmt="github"))
            input("Precione una tecla para continuar.....")
        elif(opcion == 0):
            break
def menu1():
    while True:
        print("""  
                                                                                   
            1. Eliminar una Gama
            0. Atras
          
          """)        
        opcion = int(input("\nSelecione una de las opciones: "))
        if(opcion == 1):
            idGama = input("Ingrese el id de la gama que desea eliminar: ")
            print(tabulate(deleteGama(idGama)["body"], headers="keys", tablefmt="github"))

            input("Precione una tecla para continuar.....")
        elif(opcion == 0):
            break
def menu2():
    
    while True:
        print("""  
                                                                                                                                                                                                 
            1. Actualizar una Gama
            0. Atras
          
          """)        
        opcion = int(input("\nSelecione una de las opciones: "))
        if(opcion == 1):
            id = input("Ingrese el id de la Gama que desea actualizar: ")
            print(tabulate(updateGama(id), headers="keys", tablefmt="github"))
            input("Precione una tecla para continuar.....")
        elif(opcion == 0):
            break