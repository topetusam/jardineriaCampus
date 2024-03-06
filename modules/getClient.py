import storage.cliente as cli

def searchAllClientesName():
    clienteName = list()
    for val in cli.clientes:
        codigoName=dict({
            "codigo_cliente":val.get('codigo_cliente'),
            "nombre_cliente": val.get('nombre_cliente')
            }
            )
        clienteName.append(codigoName)
        return clienteName
    
def getoneClientecodigo(codigo):
        for val in cli.clientes:
            if(val.get('codigo_cliente')==codigo):
                return {
            "codigo_cliente": val.get('codigo_cliente'),
            "nombre_cliente": val.get('nombre_cliente')

        }

def getAllClientCreditCiudad(limiteCredit, ciudad):

    clienteCredic = list()
    for val in cli.clientes:
        if(val.get('limite_credito')>= limiteCredit and val.get('ciudad')== ciudad):
                clienteCredic.append(val)
        return clienteCredic

#devuelve un listado con el nombre de todos los clientes españoles


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
         