import storage.oficina as of


def getAllCodigoCiudad():
    codigoCiudad = []
    for val in of.oficina:
        codigoCiudad.append({
            "codigo": val.get("codigo_oficina"),
            "ciudad": val.get("ciuad")
        })
    
    return codigoCiudad

#devuelve un listado con la ciudad y el telefono 
#de las oficinas de españa

def getAllCiudadTelefono(pais):
    ciudadTelefono = []
    for val in of.oficina:
        if(val.get("pais") == pais):
            ciudadTelefono.append({
                "ciudad": val.get("ciudad"),
                "telefono": val.get("telefono")
            })
    return ciudadTelefono  

import storage.oficina as of

def getAllCodigoCiudad():
    codigoCiudad = []
    for val in of.oficina:
        codigoCiudad.append({
            "codigo": val.get("codigo_oficina"),
            "ciudad": val.get("ciudad")
        })
    
    return codigoCiudad


def menu():
    print("""
          
          1. Obtener todos los clientes (nombre)
          2. Obtener un cliente por el codigo
          3. Obtener toda la informacion del cliente segun su limite de credito y ciudad que pertenece
          4. Obtener clientes por pais, region y ciudad
          5. Obtener cliente por pais
          
          """)
    opcion=int(input("Elija una de las opciones: "))
    
    
    if(opcion==1):
        print(tabulate(searchAllClientesName(), headers="keys", tablefmt = 'rounded_grid'))
    
    elif(opcion==2):
        codigoCliente= int(input("Ingrese el codigo del cliente: "))
        print(tabulate(getoneClientecodigo(codigoCliente), headers="keys", tablefmt = 'rounded_grid'))    
    
    elif(opcion == 3):
        limiteCredit = int(input("Ingrese el limite de credito de los clientes que deseas visualizar: "))
        ciudad = input("ingrese la ciudad que desea filtrar los clientes: ")
        print(tabulate(getAllClientCreditCiudad(limiteCredit, ciudad), headers="keys", tablefmt='rounded_grid'))