import os 
from tabulate import tabulate
import json
import requests
import modules.getProducto as gP


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

    peticion= requests.post("http://172.16.106.53:4501/producto", data=json.dumps(producto))
    res = peticion.json()
    res["mensaje"]="Producto Guardado"
    return [res]

def deleteProducto(id):
    data = gP.getProductCodigo(id)
    if(len(data)):
        peticion = requests.delete(f"http://172.16.106.53:4501/producto/{id}")
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


def updateProducto(id):
    producto = {
        "codigo producto": input("Ingrese el nuevo código del producto: "),
        "nombre producto": input("Ingrese el nuevo nombre del producto: "),
        "gama_producto": input("Ingrese la nueva gama del producto: "),
        "descripcion producto": input("Ingrese la nueva descripción del producto: "),
        "Dimensiones": input("Ingrese la nueva dimensión: "),
        "Proveedor": input("Ingrese el nuevo proveedor: "),
        "cantidad_en_stock": int(input("Ingrese el nuevo stock del producto: ")),
        "precio_venta": int(input("Ingrese el nuevo precio de venta: ")),
        "precio_proveedor": int(input("Ingrese el nuevo precio del proveedor: "))
    }

    producto_existente = gP.getProductCodigo(id)
    if not producto_existente:
        return {"mensaje": "Producto no encontrado"}

    producto_actualizado = {**producto_existente[0], **producto}


    peticion = requests.put(f"http://172.16.106.53:4501/producto/{id}", data=json.dumps(producto_actualizado))
    res = peticion.json()

    if peticion.status_code == 200:
        res["mensaje"] = "Producto actualizado correctamente"
    else:
        res["mensaje"] = "Error al actualizar el producto"
    
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

def menu1():
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
                                                                                                                                                    
            1. Eliminar un Producto
            0. Atras
          
          """)        
        opcion = int(input("\nSelecione una de las opciones: "))
        if(opcion == 1):
            idProducto = input("Ingrese el id del producto que desea eliminar: ")
            print(tabulate(deleteProducto(idProducto)["body"], headers="keys", tablefmt="github"))

            input("Precione una tecla para continuar.....")
        elif(opcion == 0):
            break


def menu2():
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
                                                                                                                                                    
            1. Actualizar un Producto
            0. Atras
          
          """)        
        opcion = int(input("\nSelecione una de las opciones: "))
        if(opcion == 1):
            id = input("Ingrese el id del producto que desea actualizar: ")
            print(tabulate(updateProducto(id), headers="keys", tablefmt="github"))
            input("Precione una tecla para continuar.....")
        elif(opcion == 0):
            break
