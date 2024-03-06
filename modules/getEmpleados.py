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
          