import os 
from tabulate import tabulate
import json
import requests
import modules.getGama as gG


def postProducto():
    producto = {
        "codigo producto": input("Ingrese el codigo del producto: "),
        "nombre producto": input("Ingrese el nombre del producto: "),
        "gama_producto": input("Ingrese la gama del producto: "),
        "descripcion producto": input("Ingrese la descripcion del producto: "),
        "Dimensiones": input("Ingrese la dimension: "),
        "Proveedor": input("Ingrese el proveedor: "),
        "cantidad_en_stock": int(input("Ingrese el stock del producto: ")),
        "precio_venta": int(input("Ingrese el precio de venta: ")),
        "precio_proveedor": int(input("Ingrese el precio del proveedor:"))
    }

    peticion= requests.post("http://172.16.106.89:4501", data=json.dumps(producto))
    res = peticion.json()
    res["mensaje"]="Producto Guardado"
    return [res]

def menu():
    while True:
        print("""  
    ___       __          _       _      __                         __      __                    __        
   /   | ____/ /___ ___  (_)___  (_)____/ /__________ ______   ____/ /___ _/ /_____  _____   ____/ /__      
  / /| |/ __  / __ `__ \/ / __ \/ / ___/ __/ ___/ __ `/ ___/  / __  / __ `/ __/ __ \/ ___/  / __  / _ \     
 / ___ / /_/ / / / / / / / / / / (__  ) /_/ /  / /_/ / /     / /_/ / /_/ / /_/ /_/ (__  )  / /_/ /  __/     
/_/  |_\__,_/_/ /_/ /_/_/_/ /_/_/____/\__/_/   \__,_/_/      \__,_/\__,_/\__/\____/____/   \__,_/\___/      
    ____  ____  ____  ____  __  __________________  _____                                                   
   / __ \/ __ \/ __ \/ __ \/ / / / ____/_  __/ __ \/ ___/                                                   
  / /_/ / /_/ / / / / / / / / / / /     / / / / / /\__ \                                                    
 / ____/ _, _/ /_/ / /_/ / /_/ / /___  / / / /_/ /___/ /                                                    
/_/   /_/ |_|\____/_____/\____/\____/ /_/  \____//____/                                                     
                                                                                                                                                    
            1. Guardar un producto nuevo
            0. Atras
          
          """)        
        opcion = int(input("\nSelecione una de las opciones: "))
        if(opcion == 1):
            print(tabulate(postProducto(), headers="keys", tablefmt="github"))
            input("Precione una tecla para continuar.....")
        elif(opcion == 0):
            break
