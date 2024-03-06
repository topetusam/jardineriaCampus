import storage.pago as pa

def getAllFormapagoTotal():
    FormapagoTotal = []
    for val in pa.pago:
        if val.get("forma_pago") == "PayPal":
            FormapagoTotal.append({
                "Forma_pago": val.get("forma_pago"),
                "Total": val.get("total")

        })
    return FormapagoTotal

#devuelve un listado con el codigo de cliente de aquellos clientes que realizaron algun pago en 2008, tenga en cuenta que debe eliminar aquellos codigos de cliente que aparezcan repetidos
def getAllFechaPago():
    añoPago= "2008"
    FechaPago = []
    repetidos = {}
    for val in pa.pago:
            if val.get("fecha_pago").startswith(añoPago) and val.get("codigo_cliente") not in repetidos:
                 repetidos[val.get("codigo_cliente")]=True
                 FechaPago.append({
                
                "codigo": val.get("codigo_cliente"),
                "Fecha_pago": val.get("fecha_pago"),
                "Total": val.get("total")

        })
    return FechaPago

    
