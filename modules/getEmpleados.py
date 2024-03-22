from tabulate import tabulate
import requests

def getAllEmpleado():
    #json-server storage/empleado.json -b 4504 
    peticionEM= requests.get(" http://154.38.171.54:5003/empleados")
    dataEM= peticionEM.json()
    return dataEM


def getEmpleadoCodigo(codigo):
    peticion= requests.get(f"http://154.38.171.54:5003/empleados/{codigo}")
    return[peticion.json()] if peticion.ok else []

#listado con conbre apeelido y email cuyo codigo de jefe es siete
def getAllNombreApellidoEmailJefe():
    nombreApellidoEmail = []
    for val in getAllEmpleado():
        if(val.get("codigo_jefe")==7):
                nombreApellidoEmail.append(
                {
                    "nombre": val.get("nombre"),
                    "apellidos": f"{val.get('apellido1')} {val.get('apellido2')}",
                    "email": val.get("email"),
                    "jefe": val.get("codigo_jefe")
                    }
                ) 
    return nombreApellidoEmail

#devuelve el listado de todos los jefes
def getAllPuestoNombreApellidoEmail():

    nombrePuestoApellidoEmail = []
    for val in getAllEmpleado():
         if(val.get("puesto"))!= "Representante Ventas":
              nombrePuestoApellidoEmail.append({
                   
                   "nombre": val.get("nombre"),
                   "apellidos": f"{val.get('apellido1')} {val.get('apellido2')}",
                   "email": val.get("email"),
                   "puesto": val.get("puesto"),
              })
    return nombrePuestoApellidoEmail

#devuelve el nombre, apellidos puesto email, del jefe de la empresa
def getAllNombreApellidoEmailJefempresa():
    nombreApellidoEmailJefeEmpresa = []
    for val in getAllEmpleado():
        if (val.get("codigo_jefe")) == 3 and (val.get("puesto") == "Director Oficina"):
            nombreApellidoEmailJefeEmpresa.append(
                    {
                        "nombre": val.get("nombre"),
                        "apellidos": f"{val.get('apellido1')} {val.get('apellido2')}",
                        "email": val.get("email"),
                        "jefe": val.get("codigo_jefe"),
                        "puesto": val.get("puesto")
                        }
                ) 
    return nombreApellidoEmailJefeEmpresa       

def menu():
    while True:
        print("""
            

        _______ ____                ______                __               __          
       / ____(_) / /__________     / ____/___ ___  ____  / /__  ____ _____/ /___  _____
     / /_  / / / __/ ___/ __ \   / __/ / __ `__ \/ __ \/ / _ \/ __ `/ __  / __ \/ ___/
    / __/ / / / /_/ /  / /_/ /  / /___/ / / / / / /_/ / /  __/ /_/ / /_/ / /_/ (__  ) 
    /_/   /_/_/\__/_/   \____/  /_____/_/ /_/ /_/ .___/_/\___/\__,_/\__,_/\____/____/  
                                            /_/                                     

            0. Regresar
            1. Obtener Nombre apeelido y email cuyo codigo de jefe es siete
            2. Obtener el listado de todos los jefes
            3. Obtener el listado del Director de oficina

            
            """)
        opcion=int(input("Elija una de las opciones: "))
        
        
        if(opcion==1):
            print(tabulate(getAllNombreApellidoEmailJefe(), headers="keys", tablefmt = 'rounded_grid'))
        
        elif(opcion==2):
            print(tabulate(getAllPuestoNombreApellidoEmail(), headers="keys", tablefmt = 'rounded_grid'))    
        
        elif(opcion == 3):
            print(tabulate(getAllNombreApellidoEmailJefempresa(), headers="keys", tablefmt='rounded_grid'))
        

