import os 
from tabulate import tabulate
import json
import requests
import modules.getProducto as gP
import re

def validar_codigo(codigo):
    return re.match(r'^[A-Z]{2}-\d{2}$', codigo) is not None

def validar_nombre(nombre):
    return re.match(r'^([A-Z][a-z]*\s*)+$', nombre) is not None

def validar_gama(gama):
    return re.match(r'^[A-Za-z0-9\s]+$', gama) is not None

def validar_descripcion(descripcion):
    return re.match(r'^[A-Za-z0-9\s\.,]+$', descripcion) is not None

def validar_dimensiones(dimensiones):
    return re.match(r'^\d+/\d+$', dimensiones) is not None

def validar_proveedor(proveedor):
    return re.match(r'^[^\d]+$', proveedor) is not None

def validar_numero(numero):
    return numero.isdigit()

def obtener_entrada(mensaje, validador):
    while True:
        entrada = input(mensaje)
        if validador(entrada):
            return entrada
        else:
            print("El valor ingresado no cumple con el estándar establecido. Por favor, inténtelo de nuevo.")

def postProducto():
    while True:
        producto = {
            "codigo producto": obtener_entrada("Ingrese el codigo del producto (XX-99): ", validar_codigo),
                "nombre producto": obtener_entrada("Ingrese el nombre del producto: ", validar_nombre),
                "gama_producto": obtener_entrada("Ingrese la gama del producto: ", validar_gama),
                "descripcion producto": obtener_entrada("Ingrese la descripcion del producto: ", validar_descripcion),
                "Dimensiones": obtener_entrada("Ingrese la dimension 11/99: ", validar_dimensiones),
                "Proveedor": obtener_entrada("Ingrese el proveedor: ", validar_proveedor),
                "cantidad_en_stock": input("Ingrese el stock del producto: "),
                "precio_venta": input("Ingrese el precio de venta: "),
                "precio_proveedor": input("Ingrese el precio del proveedor: ")
    }
        try:

            if not validar_codigo(producto.get("codigo producto")):
                raise Exception("El codigo producto no cumple con el estandar establecido")

            if not validar_nombre(producto.get("nombre producto")):
                raise Exception("El nombre del producto no cumple con el estandar establecido")

            if not validar_gama(producto.get("gama_producto")):
                raise Exception("La gama del producto no cumple con el estandar establecido")

            if not validar_descripcion(producto.get("descripcion producto")):
                raise Exception("La descripcion del producto no cumple con el estandar establecido")

            if not validar_dimensiones(producto.get("Dimensiones")):
                raise Exception("Las dimensiones del producto no cumplen con el estandar establecido")

            if not validar_proveedor(producto.get("Proveedor")):
                raise Exception("El proveedor del producto no cumple con el estandar establecido")

            if not validar_numero(producto.get("cantidad_en_stock")):
                raise Exception("La cantidad en stock del producto debe ser un número entero")

            if not validar_numero(producto.get("precio_venta")):
                raise Exception("El precio de venta del producto debe ser un número entero")

            if not validar_numero(producto.get("precio_proveedor")):
                raise Exception("El precio del proveedor del producto debe ser un número entero")
                
            peticion= requests.post("http://http://154.38.171.54:5008/productos", data=json.dumps(producto))
            res = peticion.json()
            res["mensaje"]="Producto Guardado"
            print(tabulate([res], headers="keys", tablefmt="github"))
            input("Precione una tecla para continuar.....")
            break
        except Exception as error:
            print(error)

def deleteProducto(id):
    data = gP.getProductCodigo(id)
    if(len(data)):
        peticion = requests.delete(f"http://http://154.38.171.54:5008/productos/{id}")
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
        "codigo producto": input("Ingrese el nuevo código del producto (FF-99): "),
        "nombre producto": input("Ingrese el nuevo nombre del producto: "),
        "gama_producto": input("Ingrese la nueva gama del producto: "),
        "descripcion producto": input("Ingrese la nueva descripción del producto : "),
        "Dimensiones": input("Ingrese la nueva dimensión (XX/XX): "),
        "Proveedor": input("Ingrese el nuevo proveedor: "),
        "cantidad_en_stock": int(input("Ingrese el nuevo stock del producto: ")),
        "precio_venta": int(input("Ingrese el nuevo precio de venta: ")),
        "precio_proveedor": int(input("Ingrese el nuevo precio del proveedor: "))
    }

    producto_existente = gP.getProductCodigo(id)
    if not producto_existente:
        return {"mensaje": "Producto no encontrado"}

    producto_actualizado = {**producto_existente[0], **producto}


    peticion = requests.put(f"http://http://154.38.171.54:5008/productos/{id}", data=json.dumps(producto_actualizado))
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
