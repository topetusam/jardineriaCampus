from tabulate import tabulate
import requests
import os


def getAllData():
    #json-server storage/producto.json -b 4501 
    peticion= requests.get("http://172.16.106.105:4501")
    data= peticion.json()
    return data

def getProductCodigo(codigo):
    peticion= requests.get(f"http://172.16.106.98:4501/producto/{codigo}")
    return[peticion.json()] if peticion.ok else []


#muestra una lista con los productos disponibles y su precio

def getAllProcuctoPrecio():
    PrecioProducto = []
    for val in getAllData():
        PrecioProducto.append({
        "nombre": val.get("nombre"),
        "precio_venta": val.get("precio_venta"),
        "precio_proveedor": val.get("precio_proveedor")
    })
    return PrecioProducto


 #Devuelva un listado con todos los productos que pertenecen a la gama ornamentales y que tienen mas de 100 unidades en stock. El listado deberá estar ordenado por su precio de venta, mostrando en primer lugar los de mayor precio           

def getAllOrnamentalesPrecio():
    ProductoOrnamentales = []
    for val in getAllData():
        if val.get("gama")=="Ornamentales" and val.get("cantidad_en_stock") > 100 and val.get("cantidad_en_stock") is not None:
            ProductoOrnamentales.append({
        "nombre": val.get("nombre"),
        "gama": val.get("gama"),
        "precio_venta": val.get("precio_venta"),
        "precio_proveedor": val.get("precio_proveedor")
    })

    ProductoOrnamentales.sort(key=lambda x: x["precio_venta"], reverse= True,)        
    return ProductoOrnamentales
#Devuelva un listado con todos los productos que pertenecen a una gama escogida por el usuario y tambien dependiendo del stock que pongan. El listado deberá estar ordenado por su precio de venta, mostrando en primer lugar los de mayor precio

def getAllProductosGamaPrecio(gama, stock):
    ProductoGamaPrecio = []
    for val in getAllData():
        if val.get("gama")==gama and val.get("cantidad_en_stock") >= stock:
            ProductoGamaPrecio.append({
        "nombre": val.get("nombre"),
        "gama": val.get("gama"),
        "precio_venta": val.get("precio_venta"),
        "precio_proveedor": val.get("precio_proveedor")
    })

    ProductoGamaPrecio.sort(key=lambda x: x["precio_venta"], reverse= True,)        
    return ProductoGamaPrecio



def menu():
    while True:
        print("""
            

        _______ ____                ____           ___     __          
    / ____(_) / /__________     / __ \___  ____/ (_)___/ /___  _____
    / /_  / / / __/ ___/ __ \   / /_/ / _ \/ __  / / __  / __ \/ ___/
    / __/ / / / /_/ /  / /_/ /  / ____/  __/ /_/ / / /_/ / /_/ (__  ) 
    /_/   /_/_/\__/_/   \____/  /_/    \___/\__,_/_/\__,_/\____/____/  
                                                                    

            0. Regresar
            1. Productos disponibles y su precio
            2. Obtiene los productos "Ornamentales" que tengan stock mas de 100 unidades
            3. escoge el producto y su stock para ver su inventario
            
            """)
        opcion=int(input("Elija una de las opciones: "))
        
        
        if(opcion==1):
            print(tabulate(getAllProcuctoPrecio(), headers="keys", tablefmt = 'rounded_grid'))
        
        elif(opcion==2):
            print(tabulate(getAllOrnamentalesPrecio(), headers="keys", tablefmt = 'rounded_grid'))    
        
        elif(opcion == 3):
            gama= input("Ingrese la gama que desea")
            stock= int(input("Ingrese el stock: "))
            print(tabulate(getAllProductosGamaPrecio(gama, stock), headers="keys", tablefmt='rounded_grid'))
            
        elif(opcion==0):
            break
    