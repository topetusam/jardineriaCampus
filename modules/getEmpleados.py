import storage.empleado as em

#listado con conbre apeelido y email cuyo codigo de jefe es siete
def getAllNombreApellidoEmailJefe(codigo):
    nombreApellidoEmail = []
    for val in em.empleados:
        if(val.get("codigo_jefe")==codigo):
                nombreApellidoEmail.append(
                {
                    "nombre": val.get("nombre"),
                    "apellidos": f"{val.get('apellido1')} {val.get('apellido2')}",
                    "email": val.get("email"),
                    "jefe": val.get("codigo_jefe")
                    }
                ) 
    return nombreApellidoEmail

def getAllPuestoNombreApellidoEmail(puesto):

    nombrePuestoApellidoEmail = []
    for val in em.empleados:
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
    for val in em.empleados:
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

