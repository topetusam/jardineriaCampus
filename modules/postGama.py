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

    peticion= requests.post("http://172.16.106.53:4502/gama", data=json.dumps(gama))
    res = peticion.json()
    res["mensaje"]="Producto Guardado"
    return [res]
def deleteGama(id):
    data = gGa.getGamaCodigo(id)
    if(len(data)):
        peticion = requests.delete(f"http://172.16.106.53:4501/gama/{id}")
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
