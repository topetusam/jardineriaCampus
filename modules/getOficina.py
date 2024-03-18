from tabulate import tabulate
import requests


def getAllOficina():
    #json-server storage/oficina.json -b 4506 
    peticionOF= requests.get("http://172.16.106.105:4506")
    dataOF= peticionOF.json()
    return dataOF


#devuelve los nombres de la ciudad con su codigo
def getAllCodigoCiudad():
    codigoCiudad = []
    for val in getAllOficina():
        codigoCiudad.append({
            "codigo": val.get("codigo_oficina"),
            "ciudad": val.get("ciudad")
        })
    
    return codigoCiudad

#devuelve un listado con la ciudad y el telefono 
#de las oficinas de españa

def getAllCiudadTelefono():
    ciudadTelefono = []
    for val in getAllOficina():
        if(val.get("pais") == "España"):
            ciudadTelefono.append({
                "ciudad": val.get("ciudad"),
                "telefono": val.get("telefono")
            })
    return ciudadTelefono  

def getAllBuscarCodigoPostal(codigo_postal):
    codigoPostal= []
    for val in getAllOficina():
        if val.get("codigo_postal")==codigo_postal:
            codigoPostal.append({
            "codigo": val.get("codigo_postal"),
            "ciudad": val.get("ciudad"),
            "telefono": val.get("telefono"),
            "linea_direccion1": val.get("linea_direccion1")
        })
    return codigoPostal

def menu():
    while True:
        print("""
            

        _______ ____                ____  _____      _            
    / ____(_) / /__________     / __ \/ __(_)____(_)___  ____ _
    / /_  / / / __/ ___/ __ \   / / / / /_/ / ___/ / __ \/ __ `/
    / __/ / / / /_/ /  / /_/ /  / /_/ / __/ / /__/ / / / / /_/ / 
    /_/   /_/_/\__/_/   \____/   \____/_/ /_/\___/_/_/ /_/\__,_/  
                                                                
            0. Regresar
            1. Obtener la ciudad y el codigo de la oficina
            2. Obtener un listado con la ciudad y el telfono de las oficinas de españa
            3. Obtener la informacion de las oficinas por su codigo postal
            
            """)
        opcion=int(input("Elija una de las opciones: "))
        
        
        if(opcion==1):
            print(tabulate(getAllCodigoCiudad(), headers="keys", tablefmt = 'rounded_grid'))
        
        elif(opcion==2):
            print(tabulate(getAllCiudadTelefono(), headers="keys", tablefmt = 'rounded_grid'))    
        
        elif(opcion == 3):
            Codigop = input("ingrese el codigo postal para acceder a los datos: ")
            print(tabulate(getAllBuscarCodigoPostal(Codigop), headers="keys", tablefmt='rounded_grid'))
        elif(opcion==0):
            break