import storage.cliente as cli
from tabulate import tabulate

#devuelve un listado con los nombres de los clientes y el codigo 
def searchAllClientesName():
    clienteName = []
    for val in cli.clientes:
        codigoName=dict({
            "codigo_cliente":val.get('codigo_cliente'),
            "nombre_cliente": val.get('nombre_cliente')
            }
            )
        clienteName.append(codigoName)
    return clienteName
#devuelve un listado segun el codigo que le indiquemos al cliente
    
def getoneClientecodigo(codigo):
    CodigoClient= []
    for val in cli.clientes:
        if(val.get('codigo_cliente')==codigo):
                CodigoClient.append({
                      "codigo_cliente": val.get('codigo_cliente'),
                        "nombre_cliente": val.get('nombre_cliente')
                    
                })
    return CodigoClient     

        

def getAllClientCreditCiudad(limiteCredit, ciudad):

    clienteCredic = list()
    for val in cli.clientes:
        if(val.get('limite_credito')>= limiteCredit and val.get('ciudad')== ciudad):
                clienteCredic.append(val)
    return clienteCredic

#Obtener informacion de los clientes por pais, region y ciudad

def getAllPaisRegionCiudad(pais, region, ciudad):
    ClientPaisRegionCiudad= []
    for val in cli.clientes:
        if val.get("pais")==pais or val.get("ciudad")==ciudad or val.get("region")==region:
            ClientPaisRegionCiudad.append({
                
                 "pais":val.get("pais"),
                 "ciudad": val.get("ciudad"),
                 "region": val.get("region")
                
            })
    
    return ClientPaisRegionCiudad
#devuelve un listado con el nombre de todos los clientes españoles

def getAllClientePais(pais):
     
     clientePais = []
     for val in cli.clientes:
               if val.get("pais")==pais:
                   clientePais.append({
                    "nombre": val.get("nombre_cliente"),
                    "pais":val.get("pais"),
                    "ciudad": val.get("ciudad"),
                    "region": val.get("region")
               })
     return clientePais

#devuelve clientes Españoles

def getAllNombreClientesEspañoles():
     
     nombreClientesEspañoles = []
     for val in cli.clientes:
               if val.get("pais")=="Spain":
                     nombreClientesEspañoles.append({
                    "nombre": val.get("nombre_cliente"),
                    "pais":val.get("pais"),
                    "ciudad": val.get("ciudad"),
                    "region": val.get("region")
               })
     return nombreClientesEspañoles

#devuelve un listado con los clientes de la ciudad de madrid, y cuyo representante de ventas tenga el codigo 11 o 30

def clientesCiudadMadrid():
      clienteCiudadMadrid= []
      elijecodigo=int(input("Escoge 30 o 11 para mostrar los resultados"))
      for val in cli.clientes:
            if val.get("region")=="Madrid":
                 if elijecodigo==11 and val.get("codigo_empleado_rep_ventas")==11:
                        clienteCiudadMadrid.append({ 
                            "nombre": val.get("nombre_cliente"),
                            "pais":val.get("pais"),
                            "ciudad": val.get("ciudad"),
                            "region": val.get("region"),
                            "codigo": val.get("codigo_empleado_rep_ventas")
                        })
                 elif elijecodigo==30 and val.get("codigo_empleado_rep_ventas")==30:
                        clienteCiudadMadrid.append({
                    "nombre": val.get("nombre_cliente"),
                    "pais":val.get("pais"),
                    "ciudad": val.get("ciudad"),
                    "region": val.get("region"),
                    "codigo": val.get("codigo_empleado_rep_ventas")

                  })

            
      return clienteCiudadMadrid     


def menu():
    while True:
          print("""
          

                    
    _______ ____                _________            __     
   / ____(_) / /__________     / ____/ (_)__  ____  / /____ 
  / /_  / / / __/ ___/ __ \   / /   / / / _ \/ __ \/ __/ _ \
 / __/ / / / /_/ /  / /_/ /  / /___/ / /  __/ / / / /_/  __/
/_/   /_/_/\__/_/   \____/   \____/_/_/\___/_/ /_/\__/\___/ 
                                                            

          0. Regresar  
          1. Obtener todos los clientes (nombre)
          2. Obtener un cliente por el codigo
          3. Obtener toda la informacion del cliente segun su limite de credito y ciudad que pertenece
          4. Obtener clientes por pais, region y ciudad
          5. Obtener cliente por pais
          6. Lista los nombres de los clientes españoles
          7. Clientes de la ciudad de madrid que tengan codigo de rep de ventas 11 o 30      
          
          """)
          opcion=int(input("\n Elija una de las opciones: "))
          if(opcion==1):
                print(tabulate(searchAllClientesName(), headers="keys", tablefmt = 'rounded_grid'))
          elif(opcion==2):
                codigoCliente= int(input("Ingrese el codigo del cliente: "))
                print(tabulate(getoneClientecodigo(codigoCliente), headers="keys", tablefmt = 'rounded_grid'))    
          elif(opcion == 3):
                limiteCredit = int(input("Ingrese el limite de credito de los clientes que deseas visualizar: "))
                ciudad = input("ingrese la ciudad que desea filtrar los clientes: ")
                print(tabulate(getAllClientCreditCiudad(limiteCredit, ciudad), headers="keys", tablefmt='rounded_grid'))
            
          elif(opcion ==4):
                pais =  input("Ingrese el pais que desea flitrar: ")
                ciudad = input("ingrese la ciudad que desea filtrar los clientes: ")
                region = input("Ingrese la region que desea filtrar")
                print(tabulate(getAllPaisRegionCiudad(pais, region, ciudad), headers="keys", tablefmt='rounded_grid'))

          elif(opcion==5):
                pais = input("Ingrese el pais que desea flitrar: ")
                print(tabulate(getAllClientePais(pais), headers="keys", tablefmt='rounded_grid'))
                
          elif(opcion==6):
                print(tabulate(getAllNombreClientesEspañoles(), headers="keys", tablefmt='rounded_grid'))
          
          elif(opcion==7):
           print(tabulate(clientesCiudadMadrid(), headers="keys", tablefmt='rounded_grid'))
          
          elif(opcion==0):
               break    
           
         

            
           
         
         
   