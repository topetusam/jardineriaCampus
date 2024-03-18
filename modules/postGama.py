import os 
from tabulate import tabulate
import json
import requests
import modules.getGama as gG


def postGama():
    gama = {

        "gama": input("Ingrese la gama del producto: "),
        "descripcion_texto": input("Ingrese la descripcion del producto: "),
        "descripcion_html": input("Ingrese la descripcion HTML: "),
        "imagen": input("Ingrese la url de la Imagen: ")
    }

    peticion= requests.post("http://172.16.106.89:4502", data=json.dumps(gama))
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
            print(tabulate(postGama(), headers="keys", tablefmt="github"))
            input("Precione una tecla para continuar.....")
        elif(opcion == 0):
            break
